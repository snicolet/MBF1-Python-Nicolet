#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line



def isFile(fname):
	try:
		f_log = open(fname,'r')
		f_log.close()
		return (fname,True)
	except IOError:
		return (fname,False)

#print isFile("carnet.txt")
#print isFile("mon_fichier.txt")


#Affichage d'un fichier a l'ecran
# while True:
# 	physique = raw_input("nom du fichier: ")
# 	if physique == "":
# 		break
# 	# verifier si le fichier existe
# 	if not isFile(physique)[1]:
# 		print "ce fichier n'existe pas"
# 	else:
# 		# afficher les lignes sur l'écran
# 		with open(physique,'r') as f:
# 			for x in f:
# 				print x,


# Stockage dans un fichier des lignes tapees par l'utilisateur
while True:
	physique = raw_input("nom du fichier: ")
	if physique == "":
		break
		# vérifier si le fichier existe
	rep = "n"
	# le fichier existe
	if isFile(physique)[1]:
		print "ce fichier existe deja"
		rep = raw_input("voulez-vous l'ecraser (y/n)? ")
	# le fichier n'existe pas ou est ecrase
	if not isFile(physique)[1] or rep in ["y","Y"]:
		with open(physique,'w') as fl:
			print "Entrer les lignes a stocker"
			print "derniere ligne END"
			s = raw_input("> ")
			while s != "END":
				fl.write(s + "\n") # ajouter car de fin de ligne
				s = raw_input("> ")
