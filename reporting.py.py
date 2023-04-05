import csv
import matplotlib.pyplot as plt

paquets = []
versions = []
cve = []

with open("vuln.txt") as csvfile:
    lecteur = csv.reader(csvfile, delimiter=',')
    for ligne in lecteur:
        paquets.append(ligne[0])
        versions.append(ligne[1])
        cve.append(ligne[2])

plt.bar(paquets, versions)
plt.title("Versions de paquets vulnérables")
plt.xlabel("Paquets")
plt.ylabel("Versions")
plt.show()
