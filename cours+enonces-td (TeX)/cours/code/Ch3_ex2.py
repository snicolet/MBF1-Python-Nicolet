#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


from math import * # importation de la librairie math

print("Soit une équation du second degré a*x^2 + b*x + c:")

a = input("Entrer le coefficient a: ")
b = input("Entrer le coefficient b: ")
c = input("Entrer le coefficient c: ")

a = float(a)
b = float(b)
c = float(c)

delta = b**2 - 4*a*c

if delta < 0:
	print("Les solutions sont complexes:")
	aux = 0 + (sqrt(-delta))*1j # création du nombre complexe sqrt(delta)
	print( (-b + aux) / (2*a) )
	print( (-b - aux) / (2*a) )
elif delta == 0:
	print("Une seule solution:")
	print( -b / (2*a) )
else:
	print("Deux solutions:")
	print( (-b + sqrt(delta)) / (2*a) )
	print( (-b - sqrt(delta)) / (2*a) )
