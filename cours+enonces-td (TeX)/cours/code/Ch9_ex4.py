#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


# On rappelle la fonction isFile.
def isFile(fname):
	try:
		f_log = open(fname,'r')
		f_log.close()
		return (fname,True)
	except IOError:
		return (fname,False)

# Récupération ou création du dictionnaire carnet
# On se place dans le répertoire voulu
import os
os.chdir("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris_Lausanne/cours/code")

from pickle import *
if isFile("carnet.txt")[1] == True:
	with open("carnet.txt","r") as f_log:
		carnet = load(f_log) # On load le dico
		
else:
	carnet = {} # on crée le dico

print "n : Introduire une nouvelle adresse"
print "r : Rechercher une adresse"
print "f : Fin"

while (True):
	action = raw_input("Que voulez-vous faire? ")
	if (action in ["n", "N"]):
		# introduire une nouvelle adresse
		nom = raw_input("Entrer un nom: ")
		if nom in carnet.keys():
			print "Ce nom existe deja..."
		else:
			anniv = raw_input("anniversaire <jour.mois.annee>: ")
			tel = raw_input("telephone: ")
			carnet[nom] = (anniv, tel)
	elif (action in ["r", "R"]):
		nom = raw_input("Entrer un nom: ")
		if nom in carnet.keys():
			print "anniversaire:", carnet[nom][0]
			print "telephone:", carnet[nom][1]
		else:
			print "Ce nom n'existe pas..."
	elif action in ["f", "F"]:
		with open("carnet.txt","w") as f_log: # mode "w": on recrée le fichier
			dump(carnet,f_log) # On dump le dico dans carnet.txt
			print carnet
			break





