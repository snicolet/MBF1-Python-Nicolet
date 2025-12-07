# -*- coding: utf-8 -*-

x = 3
print(type(x))

print("")

print(7+3)
print(7-3)
print(7*3)
print(7**3)
print(7//3)
print(7%3)

print("")

print(7/3)

print("")

from os import sys # importation de la fonction sys de la librairie os
print(sys.maxsize)

print("")

x = 2.54
print(type(x))
y = 3.0
print(type(y))

print("")

print(7.2 + 3.4)
print(7.232 - 3)
print(7 * 3.0)
print(7.0 ** 3)
print(7 / 3.23)
print(7.0 % 3)

print("")

# from math import * # importation de la librairie math
# 
# print("Soit une équation du second degré a*x^2 + b*x + c:")
# a_input = input("Entrer le coefficient a: ")
# a = float(a_input) # on convertit a_input de string en float
# b_input = input("Entrer le coefficient b: ")
# b = float(b_input)
# c_input = input("Entrer le coefficient c: ")
# c = float(c_input)
# 
# delta = b**2 - 4*a*c
# 
# if delta < 0:
# 	print("Pas de solution...")
# elif delta == 0:
# 	print("Une seule solution:")
# 	print(-b / (2*a))
# else:
# 	print("Deux solutions:")
# 	print((-b + sqrt(delta)) / (2*a))
# 	print((-b - sqrt(delta)) / (2*a))
	
print("")
	
x = 1.5 + 0.5j
print(type(x))
print(x.real)
print(x.imag)

x = 1.5 + 0.5j
y = -3 + 7j
print(x + y)
print(x - y)
print(x * y)
print(x / y)

a, b = 2, 3
c = a + b*1j # création du nombre complexe a + ib
print(c)

print("")

x = True 
y = False
print(type(x))
print(type(y))

print(not True)
print(not False)
print("")
print(3 <= 4)
print(not(3 <= 4))
print("")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print((3 <= 4) and (5 > 2))
print((3 <= 5) and (6 == 2)) 
print("")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("")

# name = input("Name? ")
# password = input("Password? ")
# if name == "James" and password == "007":
#     print("Welcome...")
# else:
#     print("Acess denied.")

print("")

s = "Hello"
print(type(s))

print("")

a = "Bonnie"
b = "Clyde"
print(a + " & " + b)
print(a*3)

print("")

a = "bonjour"
print(a[0])
print(a[1])
print(a[2])
print(a[6])
print(a[-1])
print(a[-2])
print(a[0:2])
print(a[2:7])
print(a[3:4])

print("")

s = "TIGRE"
print(s.lower())
print(s) # donc s n'est pas modifiée!
t = s.lower()
print(t) # t est une nouvelle liste créée à partit de s
print(s.replace("G","T"))
print(s) # s n'est pas modifiée!

print("")

a = "bonjour"
print(len(a))

print("")

s = "TIGRE"
for c in s:
	print(c)

print("")

phrase = input("Entrer une phrase: ")
# transforme les maj. en min.
phrase = phrase.lower()
# enleve les espaces
phrase = phrase.replace(" ", "")

print(phrase)

palindrome = True # la var bool palindrome donnera la réponse...
g = 0           	# indice 1er caractere de la liste
d = len(phrase) - 1 # indice dernier caractere de la liste

while g < d:
    if phrase[g] != phrase[d]:
        palindrome = False
        break
    else:
	    g = g + 1
	    d = d - 1
    
if palindrome == True:
	print("C'est un palindrome")
else:
	print("Ce n'est pas un palindrome")

