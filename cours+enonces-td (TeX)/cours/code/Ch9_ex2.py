#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


# création du dictionnaire carnet
carnet = {}

# effacer le fichier carnet.txt avant démo

print "n : Introduire une nouvelle adresse"
print "r : Rechercher une adresse"
print "f : Fin"

while (True): # cette boucle est exécutée tout le temps, i.e., tant qu'elle n'est pas interrompue
    action = raw_input("Que voulez-vous faire? ")
    if (action in ["n", "N"]):
        # introduire une nouvelle adresse
        nom = raw_input("Entrer un nom: ")
        if nom in carnet.keys():
            print "Ce nom existe deja..."
        else:
            anniv = raw_input("anniversaire <jour.mois.annee>: ")
            tel = raw_input("telephone: ")
            carnet[nom] = (anniv, tel)
            # on ajoute le tout dans un fichier!
            with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/cours/code/carnet.txt","a") as f_carnet:
            	f_carnet.write(nom + " " + anniv + " " + tel + "\n")
    elif (action in ["r", "R"]):
        nom = raw_input("Entrer un nom: ")
        if nom in carnet.keys():
            print "anniversaire:", carnet[nom][0]
            print "telephone:", carnet[nom][1]
        else:
            print "Ce nom n'existe pas..."
    elif action in ["f", "F"]:
    	for k in carnet.keys():
    		print k, carnet[k][0], carnet[k][1]
    	break





