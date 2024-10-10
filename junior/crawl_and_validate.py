
import pandas as pd
import subprocess
import os

def update_config(config_path, url, denomination):
    """Mettre à jour le fichier config.ts avec les nouvelles données de configuration."""
    match_url = f"{url}/**"  # Construire le motif de correspondance
    output_file_name = f"{denomination.replace(' ', '_')}.json"  # Remplacer les espaces pour éviter les erreurs de fichier

    lines = []
    with open(config_path, 'r') as file:
        lines = file.readlines()

    with open(config_path, 'w') as file:
        for line in lines:
            if 'url:' in line:
                line = f'  url: "{url}",\n'
            elif 'match:' in line:
                line = f'  match: "{match_url}",\n'
            elif 'outputFileName:' in line:
                line = f'  outputFileName: "{output_file_name}",\n'
            file.write(line)

def read_csv_and_update_config(csv_path, config_path):
    """Lire le fichier CSV, extraire l'URL et la dénomination pour chaque ligne, et mettre à jour le fichier config.ts."""
    df = pd.read_csv(csv_path)
    for index, row in df.iterrows():
        url = row['URL']
        denomination = row['Denomination']
        update_config(config_path, url, denomination)
        run_crawler()  # Exécute le crawler après chaque mise à jour de configuration

def run_crawler():
    """Changer de répertoire et exécuter le crawler en utilisant npm start."""
    try:
        os.chdir('C:/Users/junio/OneDrive/Documents/junior/junior/gpt-crawler')
        subprocess.run(["npm", "start"], check=True , shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during crawler execution: {e}")

# Chemins vers les fichiers nécessaires
csv_path = 'C:/Users/junio/OneDrive/Documents/junior/junior/output_results.csv'
config_path = 'C:/Users/junio/OneDrive/Documents/junior/junior/gpt-crawler/config.ts'

# Processus complet
read_csv_and_update_config(csv_path, config_path)
