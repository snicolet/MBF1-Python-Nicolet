#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


# import os library
import os
# get the path of the current working directory (string)
cwd = os.getcwd()

f_input = raw_input("Entrer un nom de fichier : ")
print "Recherche de ce fichier dans le répertoire courant..."
print "Le contenu du fichier " + f_input + " est:"
with open(cwd+"/"+f_input,"r") as f:
	content = f.readlines()
	c = 0		# line counter
	length = 0	# file length counter
	for l in content:
		c += 1				# we increment the counter
		length += len(l)	# we increment the length
		print str(c) + " : " + l[:-1] # we remove the last \n of line l
	print "Votre fichier contient " + str(c) + " lignes et " + str(length) + " caractères."

# note: test the program with file fichier1.txt...
