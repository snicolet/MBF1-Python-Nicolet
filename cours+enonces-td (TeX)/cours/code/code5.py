# -*- coding: utf-8 -*-

a = -1
if a < 0:
	print("a est négatif")

a = 1
if a < 0:
	print("a est négatif")

a = -3
if a < 0:
	print("a est négatif")
else:
	print("a est positif ou nul")

a = 2
if a < 0:
	print("a est négatif")
else:
	print("a est positif ou nul")

a = 5
if a < 0:
	print("a est negatif")
elif a == 0:
	print("a est nul")
else:
	print("a est positif")


a = 5
if a < 0:
	print("a est negatif")
elif (a >= 0) and (a <=5):
	print("a est compris entre 0 et 5")
elif (a >= 6) and (a <=10):
	print("a est compris entre 6 et 10")
else:
	print("a est supérieur à 10")
	
	
#for i in range(1000):
#	print(i)

voyelles = "aeiouy"
for x in "il pleut":
	if x in voyelles:
		print(x + " est une voyelle")
	elif x == " ":
		pass # ne rien faire
	else:
		print(x + " est une consonne")
		
from random import *
l = []
# la fonction randint(a,b) génère un entier
# tiré aléatoirement entre a et b compris
for i in range(1000):
	l.append(randint(0,10))
somme = 0
for i in l:
	somme += i
print(somme)

for word in ('cool', 'powerful', 'readable'):
	print('Python is ' + word)

l = []
x = 0
while (x**2 <= 1000):
	l.append(x**2)
	x += 1
print(l)



from random import *
d = {}
for i in range(1000): # boucle for sur objet range
	d[i] = randint(0,10)

# boucle for sur les clés du dico
for k in d.keys():
	print(k)

# boucle for sur les valeurs du dico
for k in d.values():
	print(k)

# boucle for sur les couples clé-valeur du dico
for k in d.items():
	print(k)



