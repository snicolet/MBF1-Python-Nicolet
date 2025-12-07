#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


from random import randint


mots = ["arbre", "grave", "piece", "nuage", "crane", "sonne", "table", "herbe", "ecrou", "mulet"]


def remplace(i, c, ch):
	ch2 = ""
	for j in range(len(ch)):
		if j == i:
			ch2 += c
		else:
			ch2 += ch[j]
	return ch2


# exemple
# print remplace(3, "x", "abracadabra")


def motus(n = 10):
	"""Jeu Motus"""
	mot_cache = mots[randint(0,len(mots)-1)]
	mot_devine = "....."
	essai = 0
	while essai < n:
		print "Essai", essai+1
		lettre = raw_input("Entrer une lettre: ")
		for j in range(len(mot_cache)):
			if mot_cache[j] == lettre:
				mot_devine = remplace(j, lettre, mot_devine)
			else: 		# useless instructions
				pass	# ...
		print "\n" + mot_devine + "\n"
		if not("." in mot_devine):
			print "Bravo!"
			break
		else:
			essai += 1
			if essai == n:
				print "Perdu!"
			
			
# We now call the procedure motus()		
motus(7) # with 7 trials