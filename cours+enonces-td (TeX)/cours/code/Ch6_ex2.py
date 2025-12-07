#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


from math import * # importation de la librairie math

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

s = solution_eq(3,7,4)
print(s[0])
print(s[1])