import os
import re
import unicodedata

KNOWLEDGE_PATH = "./Knowledge_cleaned"  # Dossier cible pour le nettoyage des noms de fichiers

def sanitize_filename(filename: str) -> str:
    # 1. Séparation stricte du radical et de l'extension
    name, ext = os.path.splitext(filename)
    ext = ext.strip().lower()

    # Correction préalable des corruptions fréquentes d'encodage (ex: UTF-8 lu en Latin-1)
    encoding_fixes = {
        "Ã©": "e", "Ã¨": "e", "Ãª": "e", "Ã«": "e",
        "Ã ": "a", "Ã¢": "a", "Ã¤": "a",
        "Ã®": "i", "Ã¯": "i",
        "Ã´": "o", "Ã¶": "o",
        "Ã¹": "u", "Ã»": "u", "Ã¼": "u",
        "Ã§": "c"
    }
    for bad_char, fixed_char in encoding_fixes.items():
        name = name.replace(bad_char, fixed_char)

    # 2. Table de remplacement direct pour toutes les voyelles et cédilles
    char_map = {
        # E
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        # A
        'à': 'a', 'â': 'a', 'ä': 'a', 'á': 'a', 'ã': 'a',
        'À': 'A', 'Â': 'A', 'Ä': 'A', 'Á': 'A', 'Ã': 'A',
        # I
        'î': 'i', 'ï': 'i', 'í': 'i', 'ì': 'i',
        'Î': 'I', 'Ï': 'I', 'Í': 'I', 'Ì': 'I',
        # O
        'ô': 'o', 'ö': 'o', 'ó': 'o', 'ò': 'o', 'õ': 'o',
        'Ô': 'O', 'Ö': 'O', 'Ó': 'O', 'Ò': 'O', 'Õ': 'O',
        # U
        'ù': 'u', 'û': 'u', 'ü': 'u', 'ú': 'u',
        'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ú': 'U',
        # Y & Cédille
        'ÿ': 'y', 'ý': 'y', 'Ÿ': 'Y', 'Ý': 'Y',
        'ç': 'c', 'Ç': 'C', 'ñ': 'n', 'Ñ': 'N'
    }
    
    # Remplacement direct
    for accented_char, clean_char in char_map.items():
        name = name.replace(accented_char, clean_char)

    # 3. Sécurité supplémentaire : décomposition Unicode pour tout accent restant
    normalized = unicodedata.normalize("NFKD", name)
    no_accents = "".join(c for c in normalized if not unicodedata.combining(c))

    # 4. Remplacement des espaces, tirets et séparateurs par un underscore
    cleaned_name = re.sub(r"[\s\t\n\-]+", "_", no_accents)

    # 5. Conservation uniquement des lettres, chiffres et underscores
    cleaned_name = re.sub(r"[^\w]", "", cleaned_name)

    # 6. Suppression des underscores multiples et de bordure
    cleaned_name = re.sub(r"_+", "_", cleaned_name).strip("_")

    if not cleaned_name:
        cleaned_name = "document"

    return f"{cleaned_name}{ext}"

def clean_directory(root_dir: str):
    if not os.path.exists(root_dir):
        print(f"Erreur : Le dossier '{root_dir}' n'existe pas.")
        return

    renamed_count = 0

    for dirpath, _, filenames in os.walk(root_dir, topdown=False):
        for filename in filenames:
            # Ignore les fichiers cachés (.DS_Store, .obsidian, etc.)
            if filename.startswith("."):
                continue

            new_filename = sanitize_filename(filename)

            if new_filename != filename:
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_filename)

                # Gestion des collisions
                counter = 1
                base_name, ext = os.path.splitext(new_filename)
                while os.path.exists(new_path) and new_path != old_path:
                    new_path = os.path.join(dirpath, f"{base_name}_{counter}{ext}")
                    counter += 1

                os.rename(old_path, new_path)
                print(f"Renommé : '{filename}' -> '{os.path.basename(new_path)}'")
                renamed_count += 1

    print(f"\nNettoyage terminé : {renamed_count} fichier(s) renommé(s).")

if __name__ == "__main__":
    clean_directory(KNOWLEDGE_PATH)