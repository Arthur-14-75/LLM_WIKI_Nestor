// Ce fichier permet de faire le lien entre le frontend et le backend. Il contient les fonctions pour interagir avec l'API du backend.

const API_BASE_URL = "http://localhost:8000"; // Remplacez par l'URL de votre backend si nécessaire

export interface QueryResponse {
    answer: string;
    sources: string[];
    }

export interface IndexResponse {
  status: string;
  indexed_files: number;
  total_chunks: number;
}

export interface WikiFileList {
    files: string[];
}

export interface WikiFileContent {
    filename: string;
    content: string;
}

export const fetchWikiFileList = async (): Promise<WikiFileList> => {
    const response = await fetch(`${API_BASE_URL}/list_wiki_files`);
    if (!response.ok) throw new Error("Impossible de récupérer la liste des fiches.");
    const data: WikiFileList = await response.json();
    return data;
};

export const fetchWikiFileContent = async (filename: string): Promise<WikiFileContent> => {
    const response = await fetch(`${API_BASE_URL}/get_wiki_file/${encodeURIComponent(filename)}`);
    if (!response.ok) throw new Error(`Impossible de récupérer le contenu de la fiche: ${filename}`);
    const data: WikiFileContent = await response.json();
  return data;
}

export const AskNestor = async (query: string ) : Promise<string> => {
    const response  = await fetch(`${API_BASE_URL}/ask_nestor`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
    });

    if (!response.ok) {
        throw new Error(`Erreur lors de l'appel à l'API: ${response.statusText}`);
    }

    const data: QueryResponse = await response.json();
    return data.answer;
};

export const triggerIndexation = async () : Promise<IndexResponse> => {
    const response = await fetch(`${API_BASE_URL}/index_documents`, {
        method: "POST",
    });

    if (! response.ok) {
        throw new Error(`Echec de l'indexation: ${response.statusText}`);
    }

    return response.json() as Promise<IndexResponse>;
};

export const RefreshWiki = async() :Promise<{ status: string; message: string }> => {
    const response = await fetch(`${API_BASE_URL}/wiki/update`,{
        method:'POST',
    });
    if (!response.ok) {
    const errorData = await response.json().catch(() => null);
    const detail = errorData?.detail || response.statusText;
    throw new Error(`Erreur serveur (${response.status}) : ${detail}`);
  }
    return await response.json();
}