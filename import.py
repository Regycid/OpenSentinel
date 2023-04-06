import csv

# Lecture du fichier texte
with open('graph.txt', 'r') as file:
    data = file.readlines()

# Traitement des données
rows = []
for line in data:
    row = line.strip().split(',')
    rows.append(row)

# Écriture des données dans le fichier CSV
with open('packages 2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
