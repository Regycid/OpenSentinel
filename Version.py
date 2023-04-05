import subprocess
import platform

with open('version.txt','w') as versionFile:
#Ouvre le fichier des paquets et sépare chaque ligne et champs
    with open('installed_packages.txt', 'r') as f:
        for line in f:
            if platform.system() == 'Linux': 
                fields = line.split()
#Si le 3eme champ existe, le defini dans version et ne conserve que les . et chiffres   
                if len(fields) > 2:
                    version = fields[2]
                    version = version.split('+')[0]
                    version = ''.join([c for c in version if c.isdigit() or c == '.'])
#Affiche le nom du paquet et sa version 
                    print(fields[1], version, file = versionFile)
            elif platform.system() == 'Windows':
                    fields = line.split( )
                    version = fields[1]
#Affiche le nom du paquet et sa version 
                    print(fields[0], version, file = versionFile)