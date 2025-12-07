#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


prenom = input("Entrer votre prenom: ")
nom = input("Entrer votre nom: ")
nom_complet = prenom + " " + nom
print(nom_complet)
initiales = prenom[0] + ". " + nom[0] + "."
print(initiales)
print("Premiere lettre de votre nom de famille:", nom[0])