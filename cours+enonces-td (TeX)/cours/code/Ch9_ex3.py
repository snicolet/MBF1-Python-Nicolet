#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line

date  = "17-JAN-1990"
piece = ("roi", "dame", "fou", "tour", "cavalier", "pion")
b = "blanc"
n = "noir"
joueurs = (("Karpov",b), ("Kasparov",n))
jeu = {("e",1) : (piece[0],b), ("e",3) : (piece[0],n)}
# Liste de chaîne, tuple, dictionnaire,...
liste = [date, piece, b, n, joueurs, jeu]


# On se place dans le répertoire voulu
import os
os.chdir("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris_Lausanne/cours/code")


# On crée un fichier dans lequel on stocke l'objet liste.
# On utilise l'instruction dump.
from pickle import *

with open("my_file.txt","w") as f_log:
	dump(liste,f_log) # on dump l'objet liste


# On récupère l'objet liste.
# On utilise l'instruction load.
with open("my_file.txt","r") as f_log:
	liste2 = load(f_log) # on load le contenu de f_log

# On a bien récupéré l'objet liste de départ
print type(liste2)
print liste2
for x in liste2:
	print x
	print type(x)


print liste2 == liste




