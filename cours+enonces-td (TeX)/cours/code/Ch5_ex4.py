#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


from math import * # importation de la librairie math
# pour un nombre entier n > 2, entré par l'utilisateur,
# ce programme détermine si n est premier ou non

n = input("Entrer un nombre entier positif: ")
# 0, 1 et 2 sont premiers
if (n == 0 or n == 1 or n == 2):
	premier = True
else:
	# au début, si n impair, premier = True
	# si n pair, premier = False
	premier = ((n % 2) == 1)
	diviseur = 3
	sqrtN = sqrt(n)
	# augmenter le diviseur tant qu'il est premier
	while (diviseur <= sqrtN and premier == True):
		premier = ((n % diviseur) != 0)
		# on incrémente le diviseur de 2 en 2 pour éviter les diviseurs pairs, déjà testé
		diviseur = diviseur + 2
		
if premier == True:
	print("Votre nombre est premier")
else:
	print("Votre nombre n'est pas premier")

#print(n, "est" if premier else "n'est pas", "premier")