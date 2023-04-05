import requests

#Ouvre le fichier de versions et cree celui de vulnerabilites
with open("version.txt", "r") as file, open("vulns.txt", "w") as output_file:
    for line in file:
#Separe les lignes en champs et verifie qu'il y en a 2
        package_info = line.strip().split(" ")
        if len(package_info) < 2:
            print(f"Paquet invalide: {line}")
            continue

#Passe le nom et la version de paquet dans les variables pour les remplacer dans l'url MITRE
        package_name = package_info[0]
        package_version = package_info[1]
        url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={package_name} {package_version}&resultsPerPage=200"
        response = requests.get(url)

#Verifie que la reponse est valide et exporte les resultats
        if response.status_code == 200:
            results = response.json()["result"]["CVE_Items"]
            for result in results:
                cve_id = result["cve"]["CVE_data_meta"]["ID"]
                output_file.write(f"{package_name} {package_version} {cve_id}\n")
                print(f"{package_name} {package_version} {cve_id}")
        else:
            print(f"Une erreur est arrivee avec {package_name} {package_version}")