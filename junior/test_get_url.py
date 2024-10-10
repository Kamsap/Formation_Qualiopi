
import pandas as pd
from duckduckgo_search import DDGS
import re

def clean_keywords(keywords):
    """ Nettoie les mots-clés en conservant certains caractères spéciaux. """
    clean_keywords = re.sub(r'[^\w\s\'_,\-]', '', keywords)
    return clean_keywords.strip()

def search_duckduckgo(query, max_results=10):
    ddgs = DDGS()
    excluded_domains = ['facebook', 'wikipedia', 'github', 'pagesjaunes', 'societe.com', 'linkedin']
    try:
        results = ddgs.text(keywords=query, max_results=max_results)
        for result in results:
            url = result['href']
            if not any(domain in url for domain in excluded_domains):
                return url  # Retourner la première URL acceptable
        return None  # Aucune URL acceptable n'a été trouvée
    except Exception as e:
        print(f"Failed to search DuckDuckGo for '{query}': {str(e)}")
        return None

def main():
    public_data = pd.read_csv('public_ofs_v2.csv', delimiter=';', low_memory=False, nrows=10)

    results = []
    for index, row in public_data.iterrows():
        denomination = row['denomination']
        cleaned_denomination = clean_keywords(denomination)  # Nettoyer la dénomination
        url = search_duckduckgo(cleaned_denomination, max_results=10)
        
        # Extraire les informations supplémentaires
        num_declaration = row['numeroDeclarationActivite']
        siret_etablissement = row['siretEtablissementDeclarant']
        adresse_formation = f"{row['adressePhysiqueOrganismeFormation.voie']} {row['adressePhysiqueOrganismeFormation.codePostal']} {row['adressePhysiqueOrganismeFormation.ville']}"

        results.append({
            'Denomination': denomination,
            'Cleaned Denomination': cleaned_denomination,
            'Numéro Déclaration Activité': num_declaration,
            'Siret Etablissement Déclarant': siret_etablissement,
            'Adresse Organisme Formation': adresse_formation,
            'URL': url if url else "No valid URL found", 
        })

    # Convertir les résultats en DataFrame
    results_df = pd.DataFrame(results)
    results_df.to_csv('output_results.csv', index=False)
    print("Results saved to output_results.csv")

if __name__ == '__main__':
    main()
