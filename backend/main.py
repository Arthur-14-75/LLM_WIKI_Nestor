import os
import re
import numpy as np
import traceback
from pathlib import Path
from typing import List
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.tools import tool
from langchain.agents import create_agent

from fastapi import FastAPI, HTTPException
from data_feed import fetch_arxiv_papers
from Wiki_builder import build_wiki_page

from sentence_transformers import CrossEncoder
from rank_bm25 import BM25Okapi

VAULT_PATH = Path("./Knowledge_cleaned")
WIKI_DIR = VAULT_PATH / "Wiki"
INDEX_FILE = VAULT_PATH / "index.md"
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "wiki_nestor"

EMBEDDING_MODEL = "nomic-embed-text"  # Modèle standard d'embedding Ollama
LLM_MODEL = "llama3.2:3b"

WIKI_DIR.mkdir(parents=True, exist_ok=True)

ollama_url = os.getenv("OLLAMA_BASE_URL","http://127.0.0.1:11434")

embedding_function = OllamaEmbeddings(
    model=EMBEDDING_MODEL,
    base_url=ollama_url
)
llm = ChatOllama(model=LLM_MODEL, temperature=0.2, max_tokens=512, base_url=ollama_url)

# === FAstAPI setup  & CORS ===

app = FastAPI(title = "Le Wiki de Nestor ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000"], # définit la liste des origines autorisées (ici toutes les origines) à accéder à l'API FastAPI. "*" empêche les restrictions de sécurtié (utile pdt phase de dev). En prod, il faut spécifier les origines autorisées
    allow_credentials=True, # Indique au navigateur qu'il est autorisé à inclure des informations d'authentification dans les requêtes multi-origines
    allow_methods=["*"], # spécifie les méthodes HTTP autorisées (GET, POST, PUT, DELETE, etc.) pour les requêtes multi-origines. "*" signifie que toutes les méthodes sont autorisées.
    allow_headers=["*"],
)

# ==== outils de l'agent =======

@tool
def consult_wiki_index()-> str:
    """Consulte la table des matières globale du wiki (index.md).
    Indique les concepts, chapitres et pages disponibles."""
    if not WIKI_DIR.exists():
        return "Le dossier wiki est vide."
    files = [f.name for f in sorted(WIKI_DIR.glob("*.md"))]
    if not files:
        return "Aucune fiche n'est disponible dans le wiki."
    return "Fiches disponibles dans le wiki :\n" + "\n".join(f"- {f}" for f in files)

class ReadWikiInput(BaseModel):
    filename:str = Field(description="Le nom EXACT du fichier Markdown à lire (ex: 'Theme_5_Agregation.md'). Interdit d'y mettre une question ou un sujet !")

@tool(args_schema=ReadWikiInput)
def read_wiki_page(filename: str) -> str:
    """Lit l'intégralité d'une fiche Markdown du wiki..."""
    target_name = Path(filename).name.strip()
    if not target_name.endswith(".md"):
        target_name += ".md"

    target_file = WIKI_DIR / target_name
    if target_file.exists():
        return target_file.read_text(encoding="utf-8")

    # Recherche insensible à la casse et par sous-chaîne
    stem = Path(filename).stem.lower()
    for f in WIKI_DIR.glob("*.md"):
        if stem in f.stem.lower() or f.stem.lower() in stem:
            return f.read_text(encoding="utf-8")

    return f"Fiche '{filename}' introuvable dans le wiki."

reranker_model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Ici on va mettre en application l'hypothetical Document Embedding et le reranking pour améliorer la pertinence des résultats de recherche dans le wiki. L'idée est de d'abord récupérer un ensemble de documents pertinents via la recherche vectorielle, puis de les réévaluer avec le modèle de reranking pour obtenir un classement plus précis basé sur la similarité sémantique avec la requête de l'utilisateur.

def generate_hypothetical_reponse(query:str)->str:
    """Génère un passage théorique hypothétique (HyDE) pour aligner l'espace vectoriel."""
    prompt = (
        f"Tu es un expert scientifique. Écris un paragraphe concis de cours ou de fiche technique "
        f"qui répond directement à la question suivante, comme s'il était extrait d'un wiki :\n\n"
        f"Question : {query}\n\n"
        f"Passage :"
    )

    reponse = llm.invoke(prompt)
    return reponse.content.strip()

bm25_model: Optional[BM25Okapi] = None
chunks: List = []

def tokenize_text(text: str) -> List[str]:
    """Tokenize le texte en mots pour BM25."""
    return re.findall(r'\w+', text.lower())

def reciprocal_rank_fusion(dense_docs, sparse_docs, k=60):
    """ fusionne les classements dense et sparse en utilisant Reciprocal Rank Fusion (RRF) pour améliorer la pertinence globale des résultats. """
    # Création d'un dictionnaire pour stocker les scores RRF

    scores = {}
    doc_map = {}

    for rank, doc in enumerate(dense_docs):
        doc_id = doc.page_content
        doc_map[doc_id] = doc
        scores[doc_id] = scores.get(doc_id, 0.0) + (1.0 / (k + rank + 1))

    for rank, doc in enumerate(sparse_docs):
        doc_id = doc.page_content
        doc_map[doc_id] = doc
        scores[doc_id] = scores.get(doc_id, 0.0) + (1.0 / (k + rank + 1))

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [doc_map[doc_id] for doc_id, _ in ranked]



@tool
def search_wiki_content(query:str, page_hint: Optional[str] = None):
    """Cherche des notions, théorèmes, explications ou formules LaTeX dans le wiki.
    - query : terme ou question de recherche.
    - page_hint : nom optionnel de la page cible (ex: 'entropie' ou 'Revision_Examen_final')."""
    if not os.path.exists(CHROMA_PATH):
        return "Base de données de recherche non trouvée. Veuillez d'abord indexer le wiki."

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_function,
        collection_name=COLLECTION_NAME
    )
    #1. Génération d'un passage hypothétique pour la requête (HyDE)
    try:
        hypothetical_doc = generate_hypothetical_reponse(query)
        search_query = f"{query}\n{hypothetical_doc}"
    except Exception as e:
        search_query = query  # fallback si HyDE échoue

    #2. Filtrage optionnel par page_hint pour restreindre la recherche à une fiche spécifique

    if page_hint:
        clean_hint = Path(page_hint).stem
        search_filter = {"source": {"$contains": clean_hint}}

    search_filter = None
    if page_hint:
        clean_hint = Path(page_hint).stem
        search_filter = {"source": {"$contains": clean_hint}}

    #3. Récupération large de documents pertinents via la recherche vectorielle
    try:
        if search_filter:
            retrieved_docs = vectorstore.similarity_search(search_query, k=15, filter=search_filter)
        else:
            retrieved_docs = vectorstore.similarity_search(search_query, k=15)
    except Exception:
        retrieved_docs = vectorstore.similarity_search(query, k=10)

    if not retrieved_docs:
        return "Aucun document trouvé pour la requête donnée."

    #4. Reranking des documents récupérés avec le modèle CrossEncoder pour améliorer la pertinence

    sparse_docs = []
    if bm25_model is not None and chunks :
        tokenized_query = tokenize_text(query)
        #ici on récupère les chunks les plus pertinents selon BM25
        raw_sparse_candidates = bm25_model.get_top_n(tokenized_query, chunks, n=20)

        # Application du filtre page_hint sur les résultats BM25

        if page_hint:
            clean_hint = Path(page_hint).stem.lower()
            sparse_docs = [
                d for d in raw_sparse_candidates 
                if clean_hint in Path(d.metadata.get("source", "")).stem.lower()
            ]
        else:
            sparse_docs = raw_sparse_candidates

    #5. Fusion RRF des résultats dense et sparse pour obtenir un classement final
    if sparse_docs:
        candidate_docs = reciprocal_rank_fusion(retrieved_docs, sparse_docs, k=60)
    else:
        candidate_docs = retrieved_docs

    if not candidate_docs:
        return "Aucun document trouvé pour la requête donnée."

    #6. Reranking final avec le modèle CrossEncoder pour les 10 meilleurs documents

    pairs = [(query, doc.page_content) for doc in candidate_docs[:10]]
    scores = reranker_model.predict(pairs)

    scored_docs = sorted(zip(candidate_docs, scores), key=lambda x: x[1], reverse=True)
    top_docs = [doc for doc, score in scored_docs[:5]]

    # 7. Formatage de sortie
    results = []
    for doc in candidate_docs:
        source_name = Path(doc.metadata.get("source", "source")).name
        results.append(f"--- Fiche : {source_name} ---\n{doc.page_content}")

    return "\n\n".join(results)


# ======== Définition de l'agent et de l'API FastAPI ========

tools = [consult_wiki_index, read_wiki_page, search_wiki_content]

#system_message = ("Tu es Nestor, assistant documentaire universitaire STRICTEMENT restreint au contenu d'un wiki technique.\n\n"
   # "RÈGLES FONDAMENTALES NON NÉGOCIABLES :\n"
    #"1. TU N'AS AUCUNE CONNAISSANCE GÉNÉRALE. Tes connaissances se limitent UNIQUEMENT au contenu renvoyé par tes outils.\n"
    #"2. POUR TOUTE QUESTION (sans exception), tu dois exécuter un outil (`search_wiki_content`, `read_wiki_page` ou `consult_wiki_index`) avant de prononcer le moindre mot.\n"
    #"3. ARRÊT IMMÉDIAT : Dès que tu trouves l'information, la définition ou la formule recherchée dans le retour de `search_wiki_content`, formule DIRECTEMENT ta réponse finale. Ne relance PAS un autre outil inutilement.\n"
    #"4. Si une fiche retournée par `search_wiki_content` donne déjà la formule exacte, utilise-la et cite la fiche source.\n"
    #"5. N'utilise `read_wiki_page
    # ` QUE si tu as besoin de lire tout le document et que tu disposes du nom réel du fichier `.md`. Ne passe JAMAIS une question en paramètre de `read_wiki_page.`\n"
    #"4. Rendu mathématique : Formate systématiquement les formules en LaTeX standard KaTeX ($$pour bloc,$ pour inline)."
    #"4. Si l'outil ne renvoie aucun résultat pertinent, ou si la question porte sur un sujet absent du wiki (cuisine, vie quotidienne, culture générale, etc.), tu dois OBLIGATOIREMENT répondre exactement :\n"
    #"   « Cette information ne figure pas dans le wiki Nestor. »\n"
    #"5. Il t'est STRICTEMENT INTERDIT de répondre par tes propres connaissances ou de donner une recette, une anecdote ou un fait hors du wiki.\n"
    #"6. Cite toujours le nom du fichier source utilisé pour formuler ta réponse."
#)

system_message = (
    """Tu es Nestor, l'assistant expert scientifique du wiki.
Tu réponds toujours en français, avec clarté, rigueur et concision.

GESTION DES CONNAISSANCES ET DES OUTILS :
1. Tu as accès aux outils `consult_wiki_index`, `search_wiki_content` et `read_wiki_page`.
    - Si l'utilisateur mentionne un nom de fichier spécifique (ex. se terminant par .md ou un titre de document explicite), tu dois OBLIGATOIREMENT appeler en priorité `read_wiki_page`.
    - Utilise `search_wiki_content` UNIQUEMENT pour les questions thématiques sans document cible précis.
2. QUESTIONS SUR LE WIKI LUI-MÊME : Lorsque l'utilisateur te demande quels sont les documents, cours, articles ou fichiers disponibles/accessibles :
   - Utilise `consult_wiki_index`.
   - Réponds en listant CLAIREMENT les noms des fiches renvoyées par l'outil.
   - Ne dis JAMAIS que cette information ne figure pas dans le wiki : la liste renvoyée par `consult_wiki_index` EST la réponse attendue.
3. QUESTIONS THÉORIQUES / SCIENTIFIQUES :
   - Utilise `search_wiki_content` pour trouver les formules, définitions et notions.
   - Dès que l'information apparaît dans le retour de l'outil, synthétise-la directement et cite la fiche source.
   - Si et seulement si une notion ou question scientifique précise n'apparaît dans aucun résultat de recherche après vérification, indique poliment : "Cette notion ne figure pas dans le wiki actuel."
4. Lors de la synthèse d'une réponse, tu dois TOUJOURS citer le nom du fichier source et le tool utilisé pour l'obtenir.
"""
)

agent_executor = create_agent(model=llm, tools=tools, system_prompt=system_message)

#===== Routes API FastAPI =====

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.post("/index_documents")
def index_documents():
    """ Indexe tous les documents du wiki dans la base vectorielle Chroma pour la recherche. """

    global bm25_model, chunks
    md_files = list(WIKI_DIR.glob("*.md"))
    if not md_files:
        raise HTTPException(status_code=404, detail="Aucun fichier Markdown trouvé dans le répertoire wiki.")

    # Chargement des fichiers Markdown
    loader = DirectoryLoader(
        str(WIKI_DIR),
        glob="*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    raw_docs = loader.load()

    # Découpage sémantique des fichiers markdown en sections pour la recherche

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200,
        chunk_overlap=150,
        separators=["\n## ", "\n### ", "\n\n", "\n", " "]
        )
    
    splits = text_splitter.split_documents(raw_docs)

    # Nettoyage des métadonnées et ajout de la source

    cleaned_splits = []
    for chunk in splits:
        text = chunk.page_content.strip()
        if len(text) > 15:
            chunk.page_content = text
            cleaned_splits.append(chunk)

    # Mise à jour du modèle BM25 pour la recherche sparse

    chunks = cleaned_splits
    tokenized_corpus = [tokenize_text(doc.page_content) for doc in chunks]
    bm25_model = BM25Okapi(tokenized_corpus)
    # Création de la base vectorielle Chroma

    vectorstore = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_function,
    collection_name=COLLECTION_NAME
)
    vectorstore.delete_collection()
    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_function,
        collection_name=COLLECTION_NAME
    )

    batch_size = 32
    for i in range(0, len(cleaned_splits), batch_size):
        vectorstore.add_documents(documents=cleaned_splits[i:i + batch_size])

    return {
        "status": "success",
        "indexed_files": len(md_files),
        "total_chunks": len(cleaned_splits)
    }

class QueryRequest(BaseModel):
    query: str


@app.post("/ask_nestor")
def query_agent(request: QueryRequest):
    try:
        response = agent_executor.invoke({
            "messages": [("user", request.query)]
        })
        
        for msg in response["messages"]:
            print(f"[{msg.__class__.__name__}] : {msg.content}")

        final_answer = response["messages"][-1].content
        return {"answer": final_answer}
    except Exception as e:
        # Affiche l'erreur détaillée dans les logs Docker
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/list_wiki_files")
def list_wiki_files():
    # Liste tous les fichiers Markdown présents dans le répertoire du wiki.
    if not WIKI_DIR.exists():
        return {"files": []}
    files = [f.name for f in sorted(WIKI_DIR.glob("*.md"))]
    return {"files": files}

@app.get("/get_wiki_file/{filename}")
def get_wiki_file(filename: str):
    clean_name = Path(filename).name
    if not clean_name.endswith(".md"):
        clean_name += ".md"
    file_path = WIKI_DIR / clean_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Fiche introuvable.")
    return {"filename": clean_name, "content": file_path.read_text(encoding="utf-8")}

@app.post("/wiki/update")
def update_wiki():
    try :
        # 1. Télécharger les nouveaux articles récents
        downloaded_pdfs = fetch_arxiv_papers(query="cat:cs.AI", max_results=2)

        #2. Ensuite on télécharge chaque PDF en fiche markdown

        generated_count = 0
        for pdf in downloaded_pdfs:
            wiki_file = WIKI_DIR / f"{pdf.stem}.md"
            if not wiki_file.exists():
                build_wiki_page(pdf)
                generated_count += 1
        return {
            "status": "success", 
            "message": f"{len(downloaded_pdfs)} PDF traités, {generated_count} nouvelles fiches générées."
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))