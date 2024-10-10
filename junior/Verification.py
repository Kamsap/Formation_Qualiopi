from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

# Configuration du pilote de navigateur
service = Service('C:\\Users\\junio\\OneDrive\\Documents\\junior\\junior\\chromedriver\chromedriver.exe')
options = Options()
options.headless = True  # Le navigateur ne s'ouvre pas visuellement

# Fonction pour vérifier les données sur une page web
def verify_data_on_page(driver, url, expected_values):
    driver.get(url)
    results = {}
    try:
        # Attendez que certains éléments soient visibles ou accessibles avant de continuer
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Exemple de vérification pour plusieurs valeurs
        for key, value in expected_values.items():
            try:
                element = driver.find_element(By.XPATH, value['xpath'])
                actual_text = element.text.strip()
                results[key] = 'CORRECT' if actual_text == value['expected'] else 'INCORRECT'
            except NoSuchElementException:
                results[key] = 'Element not found'
    except TimeoutException:
        results['page_status'] = 'Timeout/Error loading page'
    return results

# Initialiser le WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Données prévues à vérifier
expected_values = {
    'Numéro Déclaration Activité': {'xpath': '//span[@id="declaration-number"]', 'expected': '123456789'},
    'Siret Etablissement Déclarant': {'xpath': '//span[@id="siret-number"]', 'expected': '98765432109876'},
    'Adresse Organisme Formation': {'xpath': '//span[@id="address"]', 'expected': '123 Rue Example, Ville, 10000'}
}

# URL à vérifier
url_to_verify = "https://ocii.fr"

# Effectuer la vérification
verification_results = verify_data_on_page(driver, url_to_verify, expected_values)

# Nettoyage : fermer le navigateur une fois terminé
driver.quit()

# Afficher les résultats
print(verification_results)

# Sauvegarder ou manipuler les résultats de vérification ici selon les besoins
