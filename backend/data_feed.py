import re
import urllib.request
from pathlib import Path
import arxiv

RAW_DIR = Path("./Knowledge_cleaned/raw_files/scientific_articles")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def sanitize_title(title:str)->str:
    "Permet de nettoyer les titres des documents avec des noms valides faciles à interpréter"
    clean = re.sub(r"[^\w\s-]", "", title)
    return re.sub(r"[-\s]+", "_", clean).strip("_")

def fetch_arxiv_papers(query:str="cat:cs.AI", max_results:int=5)->list[Path]:
    client = arxiv.Client(page_size=max_results, delay_seconds=3.0, num_retries=3)

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate  # Récupère les plus récents
    )

    downloaded_path = []

    for paper in client.results(search):
        cleaned_name = f"{sanitize_title(paper.title)}.pdf"
        dest_path = RAW_DIR / cleaned_name

        if dest_path.exists():
            print(f"L'Article {cleaned_name} est déjà présent")
            downloaded_path.append(dest_path)
            continue

        print(f"Téléchargement : {paper.title[:60]}... ({paper.entry_id})")
        # Téléchargement direct du PDF
        pdf_url = paper.pdf_url
        if not pdf_url.endswith(".pdf"):
            pdf_url += ".pdf"
        req = urllib.request.Request(
            pdf_url, 
            headers={"User-Agent": "NestorBot/1.0 (academic research tool)"}
        )
        with urllib.request.urlopen(req) as response, open(dest_path, "wb") as out_file:
            out_file.write(response.read())

        print(f"✓ Fichier enregistré : {dest_path.name}")
        downloaded_path.append(dest_path)

    return downloaded_path

# À la toute fin de backend/data_feed.py
if __name__ == "__main__":
    new_papers = fetch_arxiv_papers(query="Retrieval Augmented Generation", max_results=5)