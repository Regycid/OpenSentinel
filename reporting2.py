import csv
import matplotlib.pyplot as plt

# Ouvrir le fichier CSV
with open('graph.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    packages = {}
    
    # Lire les données ligne par ligne
    for row in csv_reader:
        package = row['Package']
        cve = row['CVE']
        
        # Ajouter les cves pour chaque paquet
        if package not in packages:
            packages[package] = 1
        else:
            packages[package] += 1
    
    # Créer le diagramme à barres
    plt.bar(packages.keys(), packages.values())
    plt.xlabel('Paquets')
    plt.ylabel('Nombre de CVEs')
    plt.title('Reporting de vulnérabilités')
    plt.show()
