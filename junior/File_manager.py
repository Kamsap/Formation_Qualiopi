import os
import time

def clean_directory(directory):
    # Chemin du répertoire contenant les fichiers CSV
    csv_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the directory.")
        return

    # Trouver le fichier le plus récent basé sur la date de modification
    latest_file = max(csv_files, key=os.path.getmtime)

    # Supprimer tous les fichiers sauf le plus récent
    for file in csv_files:
        if file != latest_file:
            os.remove(file)
            print(f"Deleted {file}")

    print(f"Kept the latest file: {latest_file}")

# Spécifie le chemin du répertoire
directory_path = r"C:\Users\junio\OneDrive\Documents\junior"

# Appeler la fonction
clean_directory(directory_path)
