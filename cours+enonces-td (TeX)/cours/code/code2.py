# -*- coding: utf-8 -*-

x = 3
print(id(x))

print("")

x = 2
print(x)
x = 5.3
print(x)
x = "bonjour"
print(x)

print("")

ma_variable = 2
x1749 = 3.5
#1ma_varibale = 3

print("")

x = 2
y = 3.5
x = y
print(x)
print(y)

print("")

x = 2
y = "bonjour"
y = x
print(x)
print(y)

print("")

x = (2.2 ** 3) / 5
print(x)

print("")

longueur = 2.5 
largeur = 3.5
surface = longueur * largeur
print(surface)

jour = "2 juin"
annee = "2002"
date = "le " + jour + " " + annee
print(date)

print("")

x = 0
x = x + 1		# on peut aussi écrire x += 1
print(x)
x = x * 3		# on peut aussi écrire x *= 3
print(x)
x = x ** 4		# on peut aussi écrire x **= 4
print(x)
x = x / 2		# on peut aussi écrire x /= 2
print(x)
x = (x * x) / (x - 1)
print(x)

chaine = "Tex"
chaine = chaine + chaine
print(chaine)
chaine = chaine * 2 # on peut aussi écrire chaine1 *= 2
print(chaine)

print("")

x, y, z = 2.5, "bonjour", True
print(x,y,z)
prenom, nom = "Alma", "C."
print("Bonjour, " + prenom + " " + nom + "!"*3)

print("")


nom = input("Quel est votre nom? ")
prenom = input("Quel est votre prénom? ")
print(prenom + " " + nom)

age = input("Quel est votre âge? ")
print("Vous avez " + age + " ans.")
print("Dans " + str(100 - int(age)) + " ans, vous aurez 100 ans.")


