#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


from math import * # importation de la librairie math
from random import * # importation de la librairie random


# on génère le cours d'une action de 1000 valeurs
# le cours varie de +/- 2 à chaque pas de temps

def procedure_action(temps = 1000, v_init = 80, v_achat = 75, v_vente = 85):
	"""
	procedure qui implémente le cous aléatoire
	d'une action ainsi qu'une stratégie d'achat et
	de vente de cette action
	"""
	# on initialise le 1er élément de la liste
	cours = [v_init]

	# on crée les 999 éléments restants de la liste
	for i in range(temps-1):
		cours.append( cours[-1] + randint(-2,2) )
	print(cours)

	# on implémente une stratégie d'achat et de de vente
	# on suppose qu'on a achat les actions au départ
	ordre = "achat"
	for i in range(temps-1):
		# si l'action monte en-dessus de 85, on vend
		# (pour autant qu'on avait achat auparavant)
		if (cours[i] >= v_vente and ordre == "achat"):
			print("Vendre au temps", i)
			ordre = "vente"
		# si l'action baisse en-dessous de 75, on achète
		# (pour autant qu'on avait vente auparavant)
		elif (cours[i] <= v_achat and ordre == "vente"):
			print("Acheter au temps", i)
			ordre = "achat"

#print(procedure_action.__doc__)

procedure_action(v_init = 100, v_achat = 70, v_vente = 90, temps = 3000)