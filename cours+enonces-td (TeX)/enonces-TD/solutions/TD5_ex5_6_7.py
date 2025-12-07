#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


# construct dico from file
def resultatsTest(nom_fichier):
	donnees = {}
	with open(nom_fichier, 'r') as f:
		for ligne in f:
			ligne = ligne.rstrip("\n") # remove the final \n
			
			donnees_etudiant = ligne.split(",")
			prenom = donnees_etudiant[0]
			nom = donnees_etudiant[1]
			
			donnees[prenom + " " + nom] = donnees_etudiant		
	return donnees

# print info from list of personal data
def affichageEtudiant(l):
	prenom = l[0]
	nom = l[1]
	faculte = l[2]
	note = l[3]
	bonus = l[4]
	
	print "L'etudiant(e)", prenom, nom, "de la faculte", faculte, \
	"a obtenu la note de", note, "avec un bonus de", bonus, "."

# print info from dico of persons
def affichageTest(donnees, note_min = 9.5):
	for e in donnees.keys():
		note = float(donnees[e][3])
		if note > note_min:
			affichageEtudiant(donnees[e])
			

print("------- .1 -------")

donnees_test = resultatsTest("etudiants.csv")

print(donnees_test)

print("------- .2 -------")

print("Affichage des donnees d'un etudiant dans le fichier :")

affichageEtudiant(donnees_test["Eric Clark"])

print("------- .3 -------")

print("Affichage de tous les etudiants avec note minimale de 7.5")
affichageTest(donnees_test, 7.5)

print("Affichage de tous les etudiants avec note minimale de 9.5 (par defaut)")
affichageTest(donnees_test)



# Exercice suivant
donnees_test = resultatsTest("etudiants.csv")

while True:
    nom = raw_input("Entrez le prenom et le nom d'un etudiant separes par un espace \
    \n(Tapez enter pour terminer): ")
    if nom == "":
        print("Fin.")
        break
    if nom not in donnees_test.keys():
        print("l'etudiant n'existe pas dans le fichier... Veuillez reiterer votre saisie.")
        continue
    affichageEtudiant(donnees_test[nom])
    
    
# Exercice suivant
def enregistrerDonnees(donnees, fichier, faculte = ""):
	# we open the file in append mode (in order not to loose our two students)
	with open(fichier, 'a') as fh:
		compteur = 0
		for e in donnees.keys():
			if faculte != "": # si la faculte a bien ete specifiee
				if donnees[e][2] != faculte:
					# si la faculte n'est pas celle specifiee
					# on passe a l'etudiant suivant.
					continue
				else:
					fh.write(",".join(donnees[e])+"\n")
					compteur += 1
	print(compteur, "lignes ont ete ecrites dans le fichier", fichier)
                 

enregistrerDonnees(donnees_test, "etudiants.csv")
enregistrerDonnees(donnees_test, "test-droit.csv", "droit")