#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line



# importation de la librairie random
from random import *

score = 0
reponse = "gagné"
while reponse == "gagné":
	x = randint(0,1)
	if x == 0:
		x = "pile"
	else:
		x = "face"
	entree = input("pile ou face? ")
	if entree == x:
		print("vous avez gagné")
		print("vous pouvez rejouer")
		score += 1 # incrémente le score
	else:
		print("vous avez perdu")
		reponse = "perdu" # interrompt la boucle while
		print("votre score est:", score)
		
		
