#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 *** #
print "# *** 1 *** #"

prenom = raw_input("Entrer le prenom de l'etudiant: ")
nom = raw_input("Entrer le nom de l'etudiant: ")
matricule = raw_input("Entrer le matricule de l'etudiant: ")
etudiant = (prenom, nom, matricule)
print etudiant


# *** 2 *** #
print "# *** 2 *** #"

liste_etudiants = [] # empty list
while True:
	prenom = raw_input("Entrer le prenom de l'etudiant (entrer FIN pour terminer la saisie): ")
	if (prenom == "FIN") or (prenom == "fin"):
		break
	else:
		nom = raw_input("Entrer le nom de l'etudiant: ")
		matricule = raw_input("Entrer le matricule de l'etudiant: ")
		etudiant = (prenom, nom, matricule)
		liste_etudiants.append(etudiant)


# *** 3 *** #
print "# *** 3 *** #"

for e in liste_etudiants:
	print "Prenom:", e[0] + ".", "Nom:", e[1]  + ".", "Matricule:", e[2] + "."

