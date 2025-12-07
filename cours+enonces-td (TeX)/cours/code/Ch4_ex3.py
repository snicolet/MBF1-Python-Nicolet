#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


# création du dictionnaire dico
carnet = {}

print("n : Introduire une nouvelle adresse")
print("r : Rechercher une adresse")
print("f : Fin")

while (True): # cette boucle est exécutée tout le temps, i.e., tant qu'elle n'est pas interrompue
	action = input("Que voulez-vous faire? ")
	if (action in ["n", "N"]):
		# introduire une nouvelle adresse
		nom = input("Entrer un nom: ")
		if nom in carnet.keys():
			print("Ce nom existe deja...")
		else:
			anniv = input("anniversaire <jour.mois.annee>: ")
			tel = input("telephone: ")
			carnet[nom] = (anniv, tel)
	elif (action in ["r", "R"]):
		nom = input("Entrer un nom: ")
		if nom in carnet.keys():
			print("anniversaire:", carnet[nom][0])
			print("telephone:", carnet[nom][1])
		else:
			print("Ce nom n'existe pas...")
	elif action in ["f", "F"]:
		for k in carnet.keys():
			print( k, carnet[k][0], carnet[k][1] )
		break






