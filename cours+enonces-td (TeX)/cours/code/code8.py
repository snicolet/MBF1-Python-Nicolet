# -*- coding: utf-8 -*-


# >>> 5/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: integer division or modulo by zero
# >>> 1 + "a"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> l = [1,2,3]
# >>> l = ["a", "b", "c"]
# >>> l[7]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> l.ma_methode()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'ma_methode'
# >>> d = {1 : "a", 2 : "b"}
# >>> d[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 3
# >>> 



a = input("Entrer un nombre: ")
b = input("Entrer un nombre: ")
try:
	print a / float(b)
except:
	print "Division par 0 interdite..."
	

# On peut specifier le type d'exception 
# On peut multiplier les blocs "except"
a = input("Entrer un nombre: ")
b = input("Entrer un nombre: ")
try:
	print a / float(b)
except ZeroDivisionError:
	print "Division par 0 interdite..."
except:
	print "Autre type d'erreur..."



while True:
	try:
		x = input("Entrer un nombre: ")
		print "Ok, ceci est un nombre"
		break
	except:
		print "Ceci n'est pas un nombre, essayez encore..."



def print_sorted(collection):
	try:
		collection.sort()
	except AttributeError:
		pass
	print collection


print_sorted([1, 3, 2])
print_sorted("acb")