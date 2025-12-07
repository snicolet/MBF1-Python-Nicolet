#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*


# Exercice 2

def isFile(fname):
	try:
		f_log = open(fname, "r")
		f_log.close()
		return True
	except IOError:
		return False


nom_fichier = raw_input("Entrer un nom de fichier: ")
if isFile(nom_fichier) == True:
	with open(nom_fichier, "r") as f:
		l = f.readlines()
		print l
	compteur = 1
	for x in l:
		print str(compteur) + ": " + x[0:len(x)-1]
		compteur += 1
else:
	print "Le fichier n'existe pas..."





