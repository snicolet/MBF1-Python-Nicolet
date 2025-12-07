#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 *** #
print "# *** 1 *** #"


# construit une liste à partir des lignes du fichiers diamonds.csv
# chaque ligne est un élément de la liste
# chaque ligne est une chaîne de caractères
with open("diamonds.csv", "r") as f:
	diamants = f.readlines()

print len(diamants)

print diamants[0]
print diamants[1]
print diamants[2]


# *** 2 *** #
print "# *** 2 *** #"

print diamants[2].split(",")


# On modifie notre liste de sorte à ce qu'elle devienne une liste de listes
# chaque ligne du fichier, au lieu d'être une chaîne, devient une liste
i = 0
for x in diamants:
	diamants[i] = x.split(",")
	i += 1
	
print diamants[2]



# *** 3 *** #
print "# *** 3 *** #"

diamants_100 = diamants[1:100]
print diamants_100[0:20]



# *** 4 *** #
print "# *** 4 *** #"

diamants_prix = []
for x in diamants[1:]:
	diamants_prix.append(float(x[4]))
	
print diamants_prix[0:20]





	
