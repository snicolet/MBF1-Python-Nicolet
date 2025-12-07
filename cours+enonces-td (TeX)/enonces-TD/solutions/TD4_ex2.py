#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


mon_texte = "We introduce here the Python language. To learn more about the language, consider going through the excellent tutorial https://docs.python.org/ tutorial. Dedicated books are also available, such as http://www.diveintopython.net/."


def nb_car(texte):
	return len(texte)

print(nb_car(mon_texte))


def nb_mots(texte):
	counter = 0
	for c in texte:
		# for every symbol found, we increment the number of words
		if  (c == " "):
			counter += 1
	# we add 1 to count the last word (note counted, since not followed by a ". " but only by a ".")
	counter += 1
	return counter

print nb_mots(mon_texte)