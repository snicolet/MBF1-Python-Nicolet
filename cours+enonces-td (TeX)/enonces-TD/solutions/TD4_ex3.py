#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 et 2 *** #
print "# *** 1 et 2 *** #"

def TableMult(n, debut = 1, fin = 10):
	print "Fragment de la table de multiplication de", n, ":"
	if debut <= fin:
		for i in range(debut, fin+1):
			print i, 'x', n, '=', i * n
			i = i + 1
	else:
		for i in range(debut, fin-1, -1):
			print i, 'x', n, '=', i * n
			i = i + 1
		

#TableMult(7,4,12)
#TableMult(8,13,3)


# *** 3 *** #
print "# *** 3 *** #"

def TableMult2():
	n = input("Quelle base? ")
	debut = input("Debut: ")
	fin = input("Fin: ")
	print "Fragment de la table de multiplication de", n, ":"
	if debut <= fin:
		for i in range(debut, fin+1):
			print i, 'x', n, '=', i * n
			i = i + 1
	else:
		for i in range(debut, fin-1, -1):
			print i, 'x', n, '=', i * n
			i = i + 1
		

#TableMult2()
#TableMult2()