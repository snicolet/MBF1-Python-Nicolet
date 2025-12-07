#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line


from random import *
n1 = randint(0,100)
n2 = -1

while n2 != n1:
	n2 = input("Esssayer de deviner le nombre: ")
	if n2 < n1:
		print "plus haut..."
	elif n2 > n1:
		print "plus bas..."
print "Correct!"
