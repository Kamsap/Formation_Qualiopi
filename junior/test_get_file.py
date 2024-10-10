import requests
import os

def download_file():
    # URL directe du fichier CSV
    download_url = "https://www.data.gouv.fr/fr/datasets/r/ac59a0f5-fa83-4b82-bf12-3c5806d4f19f"
    
    # Chemin où sauvegarder le fichier
    directory = r"C:\Users\junio\Downloads\junior\junior"
    file_path = os.path.join(directory, 'public_ofs_v2.csv')
    
    # S'assurer que le répertoire existe
    os.makedirs(directory, exist_ok=True)
    
    # Effectuer la requête pour télécharger le fichier
    response = requests.get(download_url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Écrire le contenu dans un fichier local
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {file_path}")
    else:
        print("Failed to download the file. Status code:", response.status_code)

# Exécuter la fonction
download_file()
