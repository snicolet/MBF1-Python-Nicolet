#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 *** #
print "# *** 1 *** #"

jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mois = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

mj = []
for i in range(12):
	mj.append((mois[i], jours[i]))

print mj


# *** 2 *** #
print "# *** 2 *** #"

annee = []
for x in mj:
	for y in range(x[1]):
		annee.append(str(y+1) + " " + x[0])

print annee


# *** 3 *** #
print "# *** 3 *** #"

annee2 = []
jours_semaine = ["Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in range(365):
	annee2.append(jours_semaine[x%7] + " " + annee[x])
	
print annee2


# *** 4 *** #
print "# *** 4 *** #"

dico_annee = {}
for i in range(365):
	dico_annee[annee[i]] = jours_semaine[i%7]

print dico_annee


# *** 5 *** #
print "# *** 5 *** #"

print dico_annee["28 October"]