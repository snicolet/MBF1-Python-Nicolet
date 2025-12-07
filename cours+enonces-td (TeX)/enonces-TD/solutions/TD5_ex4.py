#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line



import os
# get the path of the current working directory (string)
cwd = os.getcwd()

# initialize an empty list 
l = []

# read the file and create the list
f_input = raw_input("Entrer un nom de fichier : ")
with open(cwd+"/"+f_input,"r") as f:
	for x in f.readlines():
		l.append(int(x[:-1]))
# note: we removed the last \n character of x
# in order to convert it in an int

# print list and its sum
print l
som = 0
for x in l:
	som += x
print "la somme des éléments est:", som


# test the program with file list.txt.
