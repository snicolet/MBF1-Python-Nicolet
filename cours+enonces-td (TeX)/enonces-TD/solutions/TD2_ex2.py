#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


# *** 1 *** #
print "# *** 1 *** #"

# Point (a)

texte = "We introduce here the Python language"

counter = 0
for c in texte:
	counter += 1
print counter
print len(texte)

# Point (b)

counter = 0
for c in texte:
	if  c != " ":
		counter += 1
print counter


# Point (c)
# Pay attention to the indentation in this exercice

counter = 0
for c in texte:
	if  c == " ": # for every space found, we increment the number of words
		counter += 1
counter += 1 # we add 1 to count the last word (note counted, since not followed by a space)
print counter


# *** 2 *** #
print "# *** 2 *** #"


# Oui, le script est toujours valable car les espaces survenant après les symboles de ponctuation permettent toujours d'incrémenter le nombre de mots.

texte2 = "We introduce here the Python language. To learn more about the language, consider going through the excellent tutorial https://docs.python.org/ tutorial. Dedicated books are also available, such as http://www.diveintopython.net/."
print texte2

counter = 0
for c in texte2:
	# for every symbol found, we increment the number of words
	if  (c == " "):
		counter += 1
# we add 1 to count the last word (note counted, since not followed by a ". " but only by a ".")
counter += 1
print counter

