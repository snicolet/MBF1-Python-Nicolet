#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


# Ce programme tire des cartes à jouer au hasard

valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
couleur = ["pique", "coeur", "carreaux", "trefle"]

from random import * # importation de la librairie random

entree = ""
while entree != "q":
	entree = input("Tapez x pour tirer une carte, q pour terminer: ")
	if entree == "x":
		# tirer une valeur au hasard
		v = randint(0,12)
		#print v
		# tirer une couleur au hasard
		c = randint(0,3)
		#print c
		print(str(valeur[v]) + " de " + couleur[c])
	elif entree == "q":
		print("Tirage terminé...")
	else:
		print("Erreur...")
