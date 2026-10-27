import os
import re
import json
import tqdm
from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

VAULT =Path("./Knowledge_cleaned")  # Chemin vers le répertoire contenant les documents
RAW_VAULT = VAULT / "raw_files"  # Chemin vers le sous-répertoire contenant les documents bruts
SCIENTIFIC_VAULT = RAW_VAULT/"scientific_articles"
WIKI_DIR = VAULT / "Wiki"  # Chemin vers le sous-répertoire contenant les documents wiki
CONCEPTS_DIR = WIKI_DIR / "concepts"  # Chemin vers le sous-répertoire contenant les pages de concepts
WIKI_DIR.mkdir(parents=True, exist_ok=True)  # Crée le répertoire Wiki s'il n'existe pas
CHROMA_PATH = "./chroma_db"
# On configure Docling sans OCR pour les PDF scannés

pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = False  # Désactive l'OCR pour les PDF scannés
converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)



COLLECTION_NAME = "wiki_nestor"
EMBEDDING_MODEL = "nomic-embed-text"  # Modèle standard d'embedding Ollama
LLM_MODEL = "llama3.2:3b"

ollama_url = os.getenv("OLLAMA_BASE_URL","http://127.0.0.1:11434")

# initialisation des embeddings et du LLM
embedding_function = OllamaEmbeddings(model=EMBEDDING_MODEL)
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0.1,
    repeat_penalty=1.15,
    num_ctx=16384,        # Permet de lire les notes sans saturer la mémoire
    num_predict=4096,     # Autorise une synthèse longue (plusieurs pages)
    base_url=ollama_url 
)
def extract_full_markdown_from_pdf(RAW_VAULT: Path) -> str:
    result = converter.convert(str(RAW_VAULT))
    return result.document.export_to_markdown()

def sanitize_latex(text: str) -> str:
    cleaned = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    cleaned = re.sub(r"\\\[([\s\S]*?)\\\]", r"$$\n\1\n$$", cleaned)
    cleaned = re.sub(
        r"(?:\r?\n|^)\s*\[\s*([a-zA-Z0-9\\_^{}\(\)\s=+\-*/.]+)\s*\]\s*(?:\r?\n|$)",
        r"\n$$\n\1\n$$\n",
        cleaned
    )

    # Supprime les titres vides résiduels du type "### Formule 7\n\n### Formule 8"
    cleaned = re.sub(r"(?:###|\*\*)\s*(?:Formule|Equation|Point)\s*\d+[\s\S]*?(?=(?:###|\*\*|$))", 
                     lambda m: "" if len(m.group(0).strip().splitlines()) <= 1 else m.group(0), 
                     cleaned)

    # Déduplication des puces numérotées répétant la même formule
    lines = cleaned.splitlines()
    seen_patterns = set()
    dedup_lines = []

    for line in lines:
        stripped = line.strip()
        
        # Isoler le contenu mathématique / textuel sans le numéro (ex: "10. " -> "")
        core_content = re.sub(r"^\d+[\.\)]\s*", "", stripped)
        # Supprimer les espaces pour comparer le squelette de l'équation
        norm_key = re.sub(r"\s+", "", core_content)

        if len(norm_key) > 8:
            if norm_key in seen_patterns:
                continue  # Ligne déjà vue : on ignore la répétition
            seen_patterns.add(norm_key)

        dedup_lines.append(line)

    return "\n".join(dedup_lines)


def extract_key_concepts(paper_summary:str) -> list[str]:
    """Extrait les concepts clés pour créer ou mettre à jour des pages de concepts."""

    prompt = f""" Tu es un architecte de connaissances. À partir de cette fiche d'article, identifie entre 2 et 6 concepts scientifiques clés majeurs (théorèmes, algorithmes, ou objets mathématiques précis).
                Pour chaque concept, fournis :
                1. "name" : Nom canonique court (ex: "Clustering spectral", "Entropie de Shannon")
                2. "definition" : Définition formelle avec formules en LaTeX ($$)
                3. "contribution" : Ce que CET article apporte spécifiquement à ce concept.

                Réponds UNIQUEMENT sous forme d'un tableau JSON valide, sans texte additionnel :
                [
                {{"name": "Nom", "definition": "Définition", "contribution": "Apport"}}
                ]

                Fiche article :
                {paper_summary[:5000]}"""

    response = llm.invoke(prompt)
    try:
        # Nettoyage d'éventuels backticks markdown
        content = re.sub(r"```json|```", "", response.content).strip()
        concepts = json.loads(content)
        return concepts if isinstance(concepts, list) else []
    except Exception as e:
        print(f"Erreur lors de l'extraction des concepts clés : {e}")
        return []

def update_concept_pages(concept: list[dict], wiki_dir: Path):
    """" effetue la mise à jour ou la création des pages de concepts dans le wiki. """
    safe_name = re.sub(r'[\\/*?:"<>|]', "", concept["name"]).strip().replace(" ", "_")
    concept_file = CONCEPTS_DIR / f"{safe_name}.md"

    if not concept_file.exists():
        content = f"""# {concept['name']}

            ## Définition Formelle
            {concept['definition']}

            ## Articles du Wiki traitant de ce sujet
            - [[{wiki_dir}]] : {concept['contribution']}
            """
        concept_file.write_text(content, encoding="utf-8")
        print(f"Nouvelle page de concept créée : {concept_file.name}")
    else:
        existing_content = concept_file.read_text(encoding="utf-8")
        addition = f"\n- [[{wiki_dir}]] : {concept['contribution']}"
        if f"[[{wiki_dir}]]" not in existing_content:
            concept_file.write_text(existing_content + addition, encoding="utf-8")
            print(f"  ⟳ Concept mis à jour : [[{safe_name}]] (nouvelle référence ajoutée)")

def insert_concept_links(wiki_content: str, known_concepts: list[dict]) -> str:
    """"" Insère des liens vers les pages de concepts dans le contenu de la fiche wiki. """
    if not known_concepts:
        return wiki_content

    # tissage simple entre les liens Obsidian et les noms de concepts

    linked_content = wiki_content
    for concept in known_concepts:
        clean_name = concept.replace("_", " ")
        # Remplace la première occurrence du concept par son Wikilink
        pattern = re.compile(rf"(?<!\[\[)\b({re.escape(clean_name)})\b(?!\]\])", re.IGNORECASE)
        linked_content = pattern.sub(rf"[[\1]]", linked_content, count=1)
    return linked_content

# =========== pipeline global de traitement d'un PDF vers une fiche wiki =================

def build_wiki_page(pdf_path: Path):
    print(f"\n--- Traitement complet : {pdf_path.name} ---")
    
    # 1. Lire la nouvelle source (Action 1)
    md_raw = extract_full_markdown_from_pdf(pdf_path)
    total_chars = len(md_raw)

    system_rules= (
        "RÈGLES CRITIQUES : Rédige en français académique. "
        "Formate les équations hors-ligne avec $$ sur des lignes dédiées. "
        "Exhaustivité scientifique sans phrases creuses."
    )

    prompt = f"""{system_rules}
        Source : {pdf_path.name}
        Extrait :
        {md_raw[:15000]}

        Génère la fiche wiki complète au format :
        # {pdf_path.stem}
        **Source originale** : `{pdf_path.name}`

        ## Contexte et Problématique
        ## Contributions Clés et Architecture
        ## Fondements Théoriques et Formules Mathématiques ($$)
        ## Limites et Perspectives
        """
    response = llm.invoke(prompt)
    final_wiki_content = sanitize_latex(response.content.strip())


    concepts = extract_key_concepts(final_wiki_content)
    existing_concepts = [f.stem for f in CONCEPTS_DIR.glob("*.md")]

    for c in concepts:
        update_concept_pages(c, pdf_path.stem)


    #3. On relie le document aux concepts connus dans le wiki

    all_concepts = list(set(existing_concepts + [c["name"] for c in concepts]))
    final_wiki_content = insert_concept_links(final_wiki_content, all_concepts)

    #4. On intègre la nouvelle source dans le wiki
    wiki_file = WIKI_DIR / f"{pdf_path.stem}.md"
    wiki_file.write_text(final_wiki_content, encoding="utf-8")
    print(f"✓ Fiche article enregistrée et maillée : {wiki_file.name}")

    #5. Indexation dans ChromaDB
    try:
        vectorstore = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embedding_function,
            collection_name=COLLECTION_NAME
        )

        md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "H1"), ("##", "H2")])
        splits = md_splitter.split_text(final_wiki_content)
        for split in splits:
            split.metadata["source"] = wiki_file.name
        vectorstore.add_documents(splits)
        print(f"✓ {wiki_file.name} indexé dans ChromaDB.")
    except Exception as e:
        print(f"Avertissement : échec de l'indexation Chroma ({e})")

if __name__ == "__main__":
    for paper in SCIENTIFIC_VAULT.rglob("*.pdf"):
        build_wiki_page(paper)

#build_wiki_page(RAW_VAULT / "scientific_articles/AD_WM_Action_Discriminative_World_Models_for_Counterfactual_Model_Predictive_Control.pdf")    

