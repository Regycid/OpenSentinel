# Import des données depuis le fichier CSV
import csv

with open('packages.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    data = [row for row in reader]

# Comptage des vulnérabilités par niveau de gravité
severity_counts = {}
for row in data:
    severity = row['Severity']
    if severity in severity_counts:
        severity_counts[severity] += 1
    else:
        severity_counts[severity] = 1

# Affichage du graphique
import matplotlib.pyplot as plt

colors = {'CRITICAL': 'red', 'HIGH': 'orange', 'MEDIUM': 'yellow', 'LOW': 'green', 'None': 'gray'}
fig, ax = plt.subplots()
ax.bar(severity_counts.keys(), severity_counts.values(), color=[colors[s] for s in severity_counts.keys()])
ax.set_xlabel('Niveau de gravité')
ax.set_ylabel('Nombre de vulnérabilités')
ax.set_title('Répartition des vulnérabilités par niveau de gravité')
plt.show()
