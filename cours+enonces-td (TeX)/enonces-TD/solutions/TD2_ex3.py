#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 *** #
print "# *** 1 *** #"

liste_mots = []
m1 = raw_input("Entrer un mot: ")
liste_mots.append(m1)
m2 = raw_input("Entrer un mot: ")
liste_mots.append(m2)
m3 = raw_input("Entrer un mot: ")
liste_mots.append(m3)

liste_mots.sort() # we sort the list

for m in liste_mots:
	print m


# *** 2 *** #
print "# *** 2 *** #"
liste_mots2 = []
mot = raw_input("Entrer un mot (taper FIN pour terminer la saisie): ")
while (mot != "FIN") and (mot != "fin"):
	liste_mots2.append(mot)
	mot = raw_input("Entrer un mot (taper FIN pour terminer la saisie): ")

liste_mots2.sort() # we sort the list

for m in liste_mots2:
	print m


# *** 2 (autre variante) *** #
print "# *** 2 (autre variante) *** #"
liste_mots2 = []
while True:
	mot = raw_input("Entrer un mot (taper FIN pour terminer la saisie): ")
	if (mot != "FIN") and (mot != "fin"):
		liste_mots2.append(mot)
	else:
		break

liste_mots2.sort() # we sort the list

for m in liste_mots2:
	print m

	
