# -*- coding: utf-8 -*-

def message():
	"""Documentation de la fonction"""
	print("Petit message")

message()
message()
print(message.__doc__)

def pi():
	"""Cette fonction retourne pi"""
	return 3.14159

print(pi())
print(pi() + 2)
print(pi.__doc__)


### *** subtilités *** ###
print("")

# argument de type non modifiable
def ma_fonction(n = 1): # ici, n prend la valeur locale par défaut 1
	n = n + 1 # n est apparemment localement modifié
	return n

print(ma_fonction(n = 5)) # n prend la valeur locale 5
print(ma_fonction()) # n possède toujours la valeur locale par défaut 1
print(ma_fonction(n = 3)) # n prend la valeur locale 3
print(ma_fonction()) # n possède toujours la valeur locale par défaut 1
n = 5 # n est modifié globalement, extérieurement à la fct
print(ma_fonction()) # n possède toujours la valeur locale par défaut 1
print(n) # valeur globale de n
print("")

# argument de type modifiable
def ma_fonction(l = [1,2,3]): # l prend la valeur locale par défaut [1,2,3]
	l.append("a") # l est modifiée localement en [1,2,3,"a"]
	return l

print(ma_fonction()) # l possède la valeur locale par défaut [1,2,3]
print(ma_fonction()) # l possède la valeur locale par défaut [1,2,3,"a"]
print(ma_fonction(l = [1,2,3,4])) # l prend la valeur locale [1,2,3,4]
l = [1,1,1] # l est modifiée globalement, extérieurement à la fct
print(ma_fonction()) # l possède la valeur locale par défaut [1,2,3,"a","a"]
print(l) # valeur globale de l
print("")

# variables locales et globales
n = 2 # n de type non modifiable (int)
l1 = [1,2,3] # l1 de type modifiable (list)
l2 = ["a","b","c"] # l2 de type modifiable (list)

def ma_fonction():
	n = 5 # réaffectation locale de n
	l1.append(4) # modification locale de l1
	l2 = [0,0,0] # réaffectation locale de l2
	print(n)
	print(l1)
	print(l2)
	
ma_fonction()
print(n) # n n'est pas modifié globalement
print(l1) # l1 est modifié globalement
print(l2) # l2 n'est pas modifié globalement (car une réaffectation locale n'est pas une modification (subtil))
print("")

n1 = 1 # n1 de type non modifiable
n2 = 2 # n2 de type non modifiable
def ma_fonction():
	n1 = 5	# réaffectation locale de n1
	global n2
	n2 = 5  # réaffectation globale de n2
	return(n1,n2)

print(ma_fonction())
print(n1) # valeur globale de n1 non modifiée
print(n2) # par contre, valeur globale de n2 modifiée!
print("")
### *** subtilités *** ###

def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)
		
print(fact(7))

print("")

from Ch6_ex4 import solution_eq
print(solution_eq(1,3,2))
from Ch6_ex4 import *
resolution_eq(1,3,2)
procedure_action()
