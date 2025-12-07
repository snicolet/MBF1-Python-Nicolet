#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line

prenom = "Astor"
nom = "Piazzolla"
nom_complet = prenom + " " + nom
print(nom_complet)
print((nom_complet + " * ")*100)
initiales = nom_complet[0] + "." + nom_complet[5:7] + "."
print(initiales)
print((initiales + " * ")*100)