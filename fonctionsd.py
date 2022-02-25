#importation
from csv import *
import json
import xml.etree.ElementTree as et
import yaml
import xmltodict
#Fontion Menu
def Menu(verif):
    verif = verif.lower()
    if verif in ['json']:
        print("Vous avez saisi un fichier",verif,"\nTapez -csv- pour convertir en format CSV\nTapez -xml- pour convertir en format XML\nTapez -yaml- pour convertir en format YAML")
    elif verif in ['yaml', 'yml']:
        print("Vous avez saisi un fichier",verif,"\nTapez -csv- pour convertir en format CSV\nTapez -xml- pour convertir en format XML\nTapez -json- pour convertir en format JSON")
    elif verif in ['xml']:
        print("Vous avez saisi un fichier",verif,"\nTapez -csv- pour convertir en format CSV\nTapez -json- pour convertir en format JSON\nTapez -yaml- pour convertir en format YAML")
    elif verif in ['csv']:
        print("Vous avez saisi un fichier",verif,"\nTapez -json- pour convertir en format Json\nTapez -xml- pour convertir en format XML\nTapez -yaml- pour convertir en format YAML")
#fonction verif fichier
def veriFichier(fichiers):
    exten = fichiers.split('.')
    if exten[-1] in ['json', 'Json', 'JSON','yaml', 'YAML', 'Ymal', 'YML','yml', 'Yml', 'csv', 'Csv', 'CSV','Xml', 'xml','XML']:
       return fichiers
    else:
        return False
#fonction recupération extension
def recupExtension(fichiers):
    ext = fichiers.split('.')
    return ext[-1]
#fonction recupération fichier
def recupFichier(fichiers):
    fichiers = fichiers.split('/')
    return fichiers[-1]
#Transform File to Dic
def transformDict(fichiers):
    dictfile=[]
    extension = fichiers.split('.')
    extension = extension[-1]
    if extension == 'yml':
        extension = 'yaml'
    if extension == 'json':
        with open(fichiers, 'r') as my_file:
            data = json.load(my_file)
            dictfile = json.dumps(data)
    elif extension == 'csv':
        with open(fichiers, 'r') as my_file:
            data = DictReader(my_file, delimiter = ';')
            for row in data:
                dictfile.append(row)
    elif extension == 'yaml':
        with open(fichiers, 'r') as my_file:
            dictfile = yaml.safe_load(my_file)
    elif extension == 'xml':
        k = open(fichiers, 'r')
        dictfile = xmltodict.parse(k.read())
    return dictfile
#Transform Dic to File
def transformToFile(choix,dictfile):
    if choix == 'json':
        with open('new.json', 'w') as y:
            json.dump(dictfile, y)
        return ("Votre fichier",choix,"a été créé")
    if choix == 'csv':
        with open('new.csv', 'w') as f:  
            writer = csv.writer(f)
            #for k, v in dictfile.items():
            writer.writerow(dictfile)
        return ("Votre fichier",choix,"a été créé")
    if choix == 'yaml':
        with open('new.yaml', 'a') as f:  
            yaml.dump(dictfile, f)
        return ("Votre fichier",choix,"a été créé")
    if choix == 'xml':
        with open('new.xml', 'w') as y:
            json.dump(dictfile, y)
        return ("Votre fichier",choix,"a été créé")
#
