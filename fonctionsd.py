#fonction Menu
import json


def Menu(verif):
    verif = verif.lower()
    if verif in ['json']:
        print("Vous avez saisi un fichier",verif,"\nTapez 1 pour convertir en format CSV\nTapez 2 pour convertir en format XML\nTapez 3 pour convertir en format YAML")
    elif verif in ['yaml', 'yml']:
        print("Vous avez saisi un fichier",verif,"\nTapez 1 pour convertir en format CSV\nTapez 2 pour convertir en format XML\nTapez 3 pour convertir en format JSON")
    elif verif in ['xml']:
        print("Vous avez saisi un fichier",verif,"\nTapez 1 pour convertir en format CSV\nTapez 2 pour convertir en format XML\nTapez 3 pour convertir en format YAML")
    elif verif in ['csv']:
        print("Vous avez saisi un fichier",verif,"\nTapez 1 pour convertir en format CSV\nTapez 2 pour convertir en format XML\nTapez 3 pour convertir en format CSV")
#fonction verif fichier
def veriFichier(fichiers):
    fichiers = fichiers.split('.')
    if fichiers[-1] in ['json', 'Json', 'JSON','yaml', 'YAML', 'Ymal', 'YML','yml', 'Yml', 'csv', 'Csv', 'CSV','Xml', 'xml','XML']:
       return fichiers
    else:
        return False
#fonction recupération extension
def recupExtension(fichiers):
    fichiers = fichiers.split('/')
    return fichiers[-1]
#fonction recupération fichier
def recupFichier(fichiers):
    fichiers = fichiers.split('/')
    fichiers = fichiers[-1]
    return fichiers
#
