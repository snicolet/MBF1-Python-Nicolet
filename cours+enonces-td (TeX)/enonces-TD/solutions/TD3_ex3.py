#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 *** #
print "# *** 1 *** #"

nb = 0
liste_notes = []
while nb < 3:
	note = input("Entrer une note: ")
	liste_notes.append(note)
	nb += 1

mini = min(liste_notes)
maxi = max(liste_notes)
moy = 0
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print "Note minimale:", mini
print "Note maximale:", maxi
print "Moyenne:", moy



# *** 2 *** #
print "# *** 2 *** #"

nb_notes = input("Combien de notes voulez-vous entrer? ")
nb = 0
liste_notes = []
while nb < nb_notes:
	note = input("Entrer une note: ")
	liste_notes.append(note)
	nb += 1

mini = min(liste_notes)
maxi = max(liste_notes)
moy = 0
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print "Note minimale:", mini
print "Note maximale:", maxi
print "Moyenne:", moy



# *** 3 *** #
print "# *** 3 *** #"

liste_notes = []
note = raw_input("Entrer une note (taper fin pour terminer la saisie): ")
while note != "fin":
	liste_notes.append(float(note))
	note = raw_input("Entrer une note (taper fin pour terminer la saisie): ")

mini = min(liste_notes)
maxi = max(liste_notes)
moy = 0
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print "Note minimale:", mini
print "Note maximale:", maxi
print "Moyenne:", moy