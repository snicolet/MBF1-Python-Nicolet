#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line

 
from math import * # importation de la librairie math
from random import * # importation de la librairie random


def resolution_eq(a,b,c):
	"""Cette procédure résout les équations du second degré de paramètres a, b, c."""
	delta = b**2 - 4*a*c
	if delta < 0:
		print "Les solutions sont complexes:"
		aux = 0 + (sqrt(-delta))*1j # création du nombre complexe sqrt(delta)
		print (-b + aux) / (2*a)
		print (-b - aux) / (2*a)
	elif delta == 0:
		print "Une seule solution:"
		print -b / (2*a)
	else:
		print "Deux solutions:"
		print (-b + sqrt(delta)) / (2*a)
		print (-b - sqrt(delta)) / (2*a)


def solution_eq(a,b,c):
	"""Cette fonction résout les équations du second degré de paramètres a, b, c et retourne les solutions."""
	delta = b**2 - 4*a*c
	if delta < 0:
		#print "Les solutions sont complexes:"
		aux = 0 + (sqrt(-delta))*1j # création du nombre complexe sqrt(delta)
		return ( (-b + aux) / (2*a), (-b - aux) / (2*a) )
	elif delta == 0:
		#print "Une seule solution:"
		return (-b / (2*a))
	else:
		#print "Deux solutions:"
		return( (-b + sqrt(delta)) / (2*a), (-b - sqrt(delta)) / (2*a) )

# on génère le cours d'une action de 1000 valeurs
# le cours varie de +/- 2 à chaque pas de temps

def procedure_action(temps = 1000, v_init = 80, v_achat = 75, v_vente = 85):
	"""procedure qui implémente de cous aléatoire d'une action ainsi qu'une stratégie d'achat et de vente de cette action"""
	# on initialise le 1er élément de la liste
	cours = [v_init]

	# on crée les 999 éléments restants de la liste
	for i in range(temps-1):
		cours.append( cours[-1] + randint(-2,2) )

	# on implémente une stratégie d'achat et de de vente
	# on suppose qu'on a achat les actions au départ
	ordre = "achat"
	for i in range(temps-1):
		# si l'action monte en-dessus de 85, on vend
		# (pour autant qu'on avait achat auparavant)
		if (cours[i] >= v_vente and ordre == "achat"):
			print "Vendre au temps", i
			ordre = "vente"
		# si l'action baisse en-dessous de 75, on achète
		# (pour autant qu'on avait vente auparavant)
		elif (cours[i] <= v_achat and ordre == "vente"):
			print "Acheter au temps", i
			ordre = "achat"
			

# procedure_action(v_init = 60, temps = 2000)