from fonctionsd import *
#Recueillir le chemin
chemin = input("Saisissez le nom du fichier(avec le chemin et l'extension)")
fichier = recupFichier(chemin)
ext = recupExtension(chemin)
#Validation de fichier et Transformation
if veriFichier(chemin) == False:
    print("Votre fichier",fichier,"n'est pas pris en compte ou valide. essayer un autre fichier")
    #chemin = input("Saisissez à nouveau le nom du fichier(avec le chemin et l'extension)")
else:
    Menu(ext)
    choix = input("Tapez votre choix ici")
    dict_file = transformDict(fichier)
    transformToFile(choix,dict_file)