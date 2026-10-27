import { useState, useEffect } from 'react'
import './App.css'
import './index.css'
import nestor from './assets/nestor.jpeg';
import Nestor2 from './assets/nestor2.png';
import Cancel from './assets/Cancel.png';
import 'katex/dist/katex.min.css';
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import { AskNestor, fetchWikiFileList,fetchWikiFileContent ,triggerIndexation, RefreshWiki } from "./services/api";

interface Message {
  Role: "user" | "Nestor";
  Content: string;
}



export  default function App() {
  const [files, setFiles] = useState<string[]>([]);
  const [selectedFile, setSelectedFile] = useState<string | null>(null);
  const [docContent, setDocContent] = useState<string>("");

  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [isUpdating, setIsUpdating] = useState<boolean>(false);
  const [indexing, setIndexing] = useState<boolean>(false);

  // chargement des fichiers au démarrage de l'application

  useEffect(() => {loadWikiFiles();}, []);

  const loadWikiFiles = async () => {
    try {
      const fileList = await fetchWikiFileList();
      setFiles(fileList.files);
    } catch (error) {
      console.error("Erreur lors du chargement des fichiers :", error);
    }
  };

  useEffect(() => {
    loadWikiFiles();
  }, []);

  function clean_latex(content:string):string {
      if(!content) return "";

      return content
      // Ici on transforme des entités HTML fréquentes dans les équations
      .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    // Supprimer les backslashes isolés en fin de ligne mathématique (ex: \theta)\ -> \theta) )
    .replace(/\\\s*$/gm, "")
    // Corriger les équations brutes sans dollar qui contiennent \prod, \sum, \frac
    .replace(/(?<!\$)\\prod_\{([^}]+)\}\^\{([^}]+)\}\s*([^\n$]+)(?!\$)/g, "$$\\prod_{\\1}^{\\2} \\3$$")
    // Normaliser \[...\]
    .replace(/\\\[([\s\S]*?)\\\]/g, (_, eq) => `$$\n${eq.trim()}\n$$`);
  }

  const handleSelectFile = async (filename: string) => {
    try {
      setSelectedFile(filename);
      const content = await fetchWikiFileContent(filename);
      setDocContent(content.content);
    } catch (error) {
      console.error("Erreur lors du chargement du contenu du fichier :", error);
    }
  };

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if( !input.trim() || loading) return;

    const userMessage = input.trim();
    setInput("");
    setMessages((prev) => [...prev, { Role: "user", Content: userMessage }]);
    setLoading(true);

    try {
      const reply = await AskNestor(userMessage);
      setMessages((prev) => [...prev, { Role: "Nestor", Content: reply }]);
    }
    catch (error) {
      console.error("Erreur lors de l'appel à l'API :", error);
      setMessages((prev) => [
        ...prev,
        { Role: "Nestor", Content: "Erreur lors de la communication avec l'agent." },
      ]);}
    finally {
      setLoading(false);
    }
  };


  const handleIndex
   = async () => {
    setIndexing(true);
    try {
      const response = await triggerIndexation();
      alert(`Indexation réussie : ${response.indexed_files} fiches indexées (${response.total_chunks} chunks).`);
    } catch (error) {
      console.error("Erreur lors de l'indexation :", error);
      alert("Erreur lors de l'indexation. Consultez la console pour plus de détails.");
    }finally {
      setIndexing(false);
    }
  };

  const handleRefreshWiki = async () => {
    if (isUpdating) return;
    setIsUpdating(true);
    try {
      await RefreshWiki();
      // Met à jour immédiatement la liste dans la barre latérale
      await loadWikiFiles();
    } catch (error) {
      console.error("Erreur lors du rafraîchissement :", error);
      alert("Échec de la mise à jour du wiki.");
    } finally {
      setIsUpdating(false);
    }
  };

  return (
    <div  style={{ display: "flex", width: "100vw", height: "100vh", overflow: "hidden" }}>
      {/* Sidebar latérale */}
      <aside
        style={{
          width: "320px",
          minWidth: "320px",
          height: "100%",
          backgroundColor: "#99300A",
          borderTopRightRadius: "40px",
          borderBottomRightRadius: "40px",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          padding: "30px 30px",
          boxSizing: "border-box",
          flexShrink: 0,
    }}

      >

        <h2 className='Wiki-nestor'>Le Wiki de Nestor</h2>

        <button
          onClick = { () => setSelectedFile(null)}
          style={{
            padding: "8px 12px",
            marginTop:"20px",
            marginBottom: "16px",
            background: selectedFile === null ? "#45475a" : "#313244",
            color: "#fff",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
            textAlign: "left",
          }}
        >
          💬 Poser une question
        </button>

        <div style={{ fontSize: "0.85rem", textTransform: "uppercase", color: "#a6adc8", marginBottom: "8px" }}>
          Fiches ({files.length})
        </div>

        <nav
          style={{
            display: "flex",
            flexDirection: "column",
            width: "100%",
            overflowY: "auto", // Permet de faire défiler la liste si elle est longue
            overflowX: "hidden",
          }}
        >
          {files.map((file) => (
            <button
              key={file}
            onClick={() => handleSelectFile(file)}
            className="fiche_bouton"
            style={{
              display: "block",
              width: "100%",
              boxSizing: "border-box",
              padding: "8px 10px",
              marginBottom: "4px",
              background: selectedFile === file ? "#45475a" : "transparent",
              color: "#cdd6f4",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
              textAlign: "left",
              whiteSpace: "nowrap",
              overflow: "hidden",
              textOverflow: "ellipsis",

              }}
              title={file}
            >
              📄 {file.replace(".md", "")}
            </button>
          ))}
        </nav>
        {/* Bouton d'actualisation calé en bas */}
        <button 
        onClick = {handleRefreshWiki}
        disabled={isUpdating}
        style = {{width: "100%",
            padding: "12px",
            backgroundColor: isUpdating ? "#6b7280" : "#ffffff",
            color: isUpdating ? "#d1d5db" : "#99300A",
            border: "none",
            borderRadius: "8px",
            fontWeight: "bold",
            cursor: isUpdating ? "not-allowed" : "pointer",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            gap: "8px",
            boxShadow: "0 2px 4px rgba(0, 0, 0, 0.2)",}}>
          {isUpdating ? "⏳ Analyse en cours..." : "🔄 Actualiser le Wiki"}
        </button>

        <div style = {{marginTop:"50px"}}>
          <img 
                src={Nestor2} 
                alt="img_renestor" 
                style={{ width: "160px", height: "190px" }} 
              />
        </div>
      </aside>
      
      {/* zone d'affichage principale*/}
      <main style={{flex: 1,
        minWidth: 0, // INDISPENSABLE en Flexbox pour forcer le respect de la largeur
        height: "100%",
        display: "flex",
        flexDirection: "column",
        padding: "24px 40px",
        boxSizing: "border-box",
        overflowY: "auto",
        overflowX: "hidden", // Empêche tout scroll horizontal global
        backgroundColor: "#FAF3E0",}}>
        {selectedFile ? (
          /* Vue consultation d'une fiche */
          <div style={{width: "100%", maxWidth: "1050px",margin: "0 auto",background: "#fff",padding: "24px",borderRadius: "8px",boxSizing: "border-box",}}>
            <div style={{display: "flex",justifyContent: "space-between",alignItems: "flex-start", gap: "16px",borderBottom: "1px solid #eee",paddingBottom: "8px",}}>
              <h2 style={{margin: 0,wordBreak: "break-word",overflowWrap: "anywhere", minWidth: 0,}}>{selectedFile}</h2>
              <button onClick={() => setSelectedFile(null)} style={{ cursor: "pointer" }}>
                <img src={Cancel} alt = "Cancel_fiche" />
              </button>
            </div>

            <div className="markdown-body" style={{marginTop: "16px",lineHeight: "1.6",wordBreak: "break-word",overflowWrap: "anywhere",maxWidth: "100%",}}>
              <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[[rehypeKatex, { throwOnError: false, strict: false }]]}>
                {clean_latex(docContent)}
              </ReactMarkdown>
            </div>
          </div>
        ): (
          /* Vue du chat/Nestor*/
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", marginBottom: "16px" }}>
            <h2 style={{ marginBottom: "12px", fontSize: "1.6rem" }}>Chat avec Nestor</h2>
            <div style={{ display: "flex", justifyContent: "center", marginBottom: "16px" }}>
                <img 
                src={nestor} 
                alt="img_nestor" 
                style={{ width: "110px", height: "110px", borderRadius: "30%", objectFit: "cover" }} 
              />
            </div>

            <div style={{flex: 1,width: "100%",overflowY: "auto",border: "1px solid #e2e8f0",borderRadius: "12px",padding: "20px",marginBottom: "16px",backgroundColor: "#fafafa",}}>
              {messages.length === 0 && <p style={{ color: "#718096", textAlign: "center", marginTop: "40px" }}>
          Sélectionne une fiche à gauche ou pose une question ici.</p>}
              {messages.map((m, idx) => (
                <div key={idx} style={{ width:"auto", marginBottom: "16px", textAlign: m.Role === "user" ? "right" : "left" }}>
                  <strong>{m.Role === "user" ? "Toi" : "Nestor"} :</strong>
                  <div
                    style={{
                      display: "inline-block",
                      background: m.Role === "user" ? "#dbeafe" : "#edf2f7",
                      color: "#1a202c",
                      padding: "10px 16px",
                      borderRadius: "8px",
                      textAlign: "left",
                      maxWidth: "100%",
                      boxSizing: "border-box",
                      overflowX: "auto", // Permet à une formule trop longue de défiler à l'intérieur de la bulle
                    }}
                  >
                    <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
                      {clean_latex(m.Content)}
                    </ReactMarkdown>


            </div>
          </div>
        ))}

      {loading && <p><em>Nestor cherche dans le wiki...</em></p>}
      </div>
      <form onSubmit={handleSend} style={{ display: "flex", width: "100%", gap: "12px" }}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Pose ta question technique..."
        style={{
          flex: 1,
          padding: "12px 16px",
          borderRadius: "8px",
          border: "1px solid #cbd5e1",
          fontSize: "1rem",
        }}
      />
      <button
        type="submit"
        disabled={loading}
        style={{
          padding: "12px 24px",
          backgroundColor: "#0284c7",
          color: "#fff",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer",
          fontWeight: 600,
        }}
      >
        Envoyer
      </button>
    </form>
      </div> )}
      </main>
      
       
    </div>
  );
}
