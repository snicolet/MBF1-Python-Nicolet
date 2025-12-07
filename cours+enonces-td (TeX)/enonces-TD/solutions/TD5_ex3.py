#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


from random import *
import os
# get the path of the current working directory (string)
cwd = os.getcwd()

n = input("Entrer un nombre entier N : ")
print "Généeration d'une liste de " + str(n) + " élémets aléatoires, chacun compris entre -100 et +100..."
# creation of the list
l = []
for i in range(int(n)-1):
	l.append(randint(-100,100))
	
# print list and som of its elements
print l
som = 0
for x in l:
	som += x
print "La somme des éléments est:", som

# save list into a specified file
f_input = raw_input("Entrer un nom de fichier : ")
with open(cwd+"/"+f_input,"w") as f:
	for x in l:
		f.write(str(x) + "\n")
		
# test the program with file list.txt for instance...