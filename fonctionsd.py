#importation
from csv import *
from json import *
import xml.etree.ElementTree as et
import yaml
import xmltodict
import dict2xml
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
    count = 0
    dictfile=[]
    extension = fichiers.split('.')
    extension = extension[-1]
    if extension == 'yml':
        extension = 'yaml'
    if extension == 'json':
        with open(fichiers, 'r') as my_file:
            data = load(my_file)
            dictfile.append(data)
    elif extension == 'csv':
        with open(fichiers, 'r') as my_file:
            data = csv.reader(my_file)#(), delimiter = ';')
            for row in data:
                if count == 0:
                    dictionfinale = row
                else:
                    verifier = dict(zip(dictionfinale, row))
                    dictfile.append(verifier)
                count += 1
                #dictfile.append(row)
    elif extension == 'yaml':
        with open(fichiers, 'r') as my_file:
            dictfile = yaml.safe_load(my_file)
    elif extension == 'xml':
        k = open(fichiers, 'r')
        dictfile = xmltodict.parse(k.read())
    return dictfile
#Transform Dic to File
def transformToFile(choix,dictfile):
    liste = []
    if choix == 'json':
        with open('new.json', 'w') as y:
            dump(dictfile, y)
        return ("Votre fichier",choix,"a été créé")
    if choix == 'csv':
        for i in range(len(dictfile)):
            elm=dictfile[i]
            keys=list(elm.keys())
        with open("mynewfile.csv","w") as csv_out:
            writer=DictWriter(csv_out,fieldnames=keys)
            writer.writeheader()
            for data in dictfile:
                writer.writerow(data)
        return ("Votre fichier",choix,"a été créé")
    if choix == 'yaml':
        with open('new.yaml', 'a') as f:  
            yaml.dump(dictfile, f)
        return ("Votre fichier",choix,"a été créé")
    if choix == 'xml':
        with open('new.xml', 'w') as y:
            contenu = dict2xml.dict2xml(dictfile)
            y.write(contenu)
        return ("Votre fichier",choix,"a été créé")
