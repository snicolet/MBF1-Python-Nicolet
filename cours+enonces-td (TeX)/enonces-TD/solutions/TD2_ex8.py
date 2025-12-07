#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 *** #
print "# *** 1 *** #"

dico_etudiants = {}	# empty dico

prenom = raw_input("Entrer le prenom de l'etudiant: ")
nom = raw_input("Entrer le nom de l'etudiant: ")
matricule = input("Entrer le matricule de l'etudiant: ")
dico_etudiants[nom] = (prenom, nom, matricule)

print dico_etudiants


# *** 2 *** #
print "# *** 2 *** #"

dico_etudiants = {}	# empty dico
while True:
	prenom = raw_input("Entrer le prenom de l'etudiant (entrer FIN pour terminer la saisie): ")
	if (prenom == "FIN") or (prenom == "fin"):
		break
	else:
		nom = raw_input("Entrer le nom de l'etudiant: ")
		matricule = input("Entrer le matricule de l'etudiant: ")
		dico_etudiants[nom] = (prenom, nom, matricule)


# *** 3 *** #
print "# *** 3 *** #"

for nom_etud in dico_etudiants:
	print "Prenom:", dico_etudiants[nom_etud][0] + ".", "Nom:", dico_etudiants[nom_etud][1]  + ".", "Matricule:", str(dico_etudiants[nom_etud][2]) + "."


# *** 4 *** #
print "# *** 4 *** #"

if "Obama" in dico_etudiants.keys():
	print "Prenom:", dico_etudiants["Obama"][0] + ".", "Nom:", dico_etudiants["Obama"][1]  + ".", "Matricule:", str(dico_etudiants["Obama"][2]) + "."


# *** 5 *** #
print "# *** 5 *** #"

for k, v in dico_etudiants.items():
	if v[2] == 12345678: # if 3rd element of tuple v is 12345678...
		print "Prenom:", dico_etudiants[k][0] + ".", "Nom:", dico_etudiants[k][1]  + ".", "Matricule:", str(dico_etudiants[k][2]) + "."


# *** 6 *** #
print "# *** 6 *** #"

dico_etudiants = {}	# empty dico
while True:
	prenom = raw_input("Entrer le prenom de l'etudiant (entrer FIN pour terminer la saisie): ")
	if (prenom == "FIN") or (prenom == "fin"):
		break
	else:
		nom = raw_input("Entrer le nom de l'etudiant: ")
		matricule = raw_input("Entrer le matricule de l'etudiant: ")
		# now, the keys are strings nom + matricule
		dico_etudiants[nom + str(matricule)] = (prenom, nom, matricule)

for nom_matricule in dico_etudiants:
	print "Prenom:", dico_etudiants[nom_matricule][0] + ".", "Nom:", dico_etudiants[nom_matricule][1]  + ".", "Matricule:", str(dico_etudiants[nom_matricule][2]) + "."



