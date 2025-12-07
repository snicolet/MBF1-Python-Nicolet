#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


from math import * # importation de la librairie math

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

resolution_eq(3,-1,4)
resolution_eq(1,4,4)
resolution_eq(4,7,-2)