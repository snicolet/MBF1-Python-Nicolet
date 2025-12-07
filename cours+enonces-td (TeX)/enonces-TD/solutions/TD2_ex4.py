#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


# *** 1 *** #
print "# *** 1 *** #"

couleurs = ['Pique', 'Trefle', 'Carreau', 'Coeur']
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as']

# Construction de la liste des 52 cartes :
cartes = []
for coul in couleurs:
	for val in valeurs:
		cartes.append(str(val) + " de " + coul)
		
print cartes


# *** 2 *** #
print "# *** 2 *** #"

from random import shuffle

shuffle(cartes)
print cartes

# *** 3 *** #
print "# *** 3 *** #"

joueur1 = []
joueur2 = []
joueur3 = []
joueur4 = []

compteur = 0
for c in cartes:
	if compteur == 0:
		joueur1.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 1:
		joueur2.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 2:
		joueur3.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 3:
		joueur4.append(c)
		compteur = (compteur + 1) % 4 

print joueur1
print joueur2
print joueur3
print joueur4
