import subprocess
import logging
import sys

# Ensure the duckduckgo_search package is installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "duckduckgo_search"])

# Now import the package
from duckduckgo_search import DDGS

def execute_script(script_path):
    """ Exécute un script Python et capture sa sortie et les erreurs potentielles. """
    try:
        result = subprocess.run(['python', script_path], text=True, capture_output=True)
        logging.info(f"Output of {script_path}: {result.stdout}")
        if result.returncode != 0:
            logging.error(f"Errors from {script_path}: {result.stderr}")
            return False
        return True
    except Exception as e:
        logging.error(f"Failed to run {script_path} with error: {e}")
        return False

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Étape 1: Télécharger le fichier depuis data.gouv
    if not execute_script('test_get_file.py'):
        logging.error("Download script failed, stopping pipeline.")
        return

    # Étape 2: Supprimer les fichiers CSV et garder le plus récent
    if not execute_script('File_manager.py'):
        logging.error("Cleanup script failed, stopping pipeline.")
        return

    # Étape 3: Rechercher les sites web des entreprises et ramener l'URL
    if not execute_script('test_get_url.py'):
        logging.error("Search script failed, stopping pipeline.")
        return

    logging.info("All scripts executed successfully.")

if __name__ == "__main__":
    main()
