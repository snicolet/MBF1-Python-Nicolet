#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


phrase = input("Entrer une phrase: ")
# transforme les maj. en min.
phrase = phrase.lower()
# enleve les espaces
phrase = phrase.replace(" ", "")

print(phrase)

palindrome = True	# la var bool palindrome donnera la réponse...
g = 0				# indice 1er caractere de la liste
d = len(phrase) - 1 # indice dernier caractere de la liste

while g < d:
	if phrase[g] != phrase[d]:
		palindrome = False
		break
	else:
		g = g + 1
		d = d - 1
		
if palindrome == True:
	print("C'est un palindrome")
else:
	print("Ce n'est pas un palindrome")

# faire le test avec la phrase "Esope reste ici et se repose"






