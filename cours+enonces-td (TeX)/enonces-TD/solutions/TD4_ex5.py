#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line




# *** 1 *** #
print "# *** 1 *** #"


def generer_grille(taille = 4):
	"""genere une grille d'une certaine taille"""
	grille = []
	for i in range(taille):
		grille.append(["."]*taille)
	return grille


# we create a grid of size 5
ma_grille = generer_grille(5)
print ma_grille




# *** 2 *** #
print "# *** 2 *** #"


def placer_pion(joueur, grille, position):
	"""place un pion dans une grille"""
	if joueur == 1:
		pion = "O"
	elif joueur == 2:
		pion = "X"
	grille[position[0]-1][position[1]-1] = pion
	return grille


	
# we place some moves
ma_grille = placer_pion(1, ma_grille, (1,3))
print ma_grille
ma_grille = placer_pion(2, ma_grille, (3,5))
print ma_grille
ma_grille = placer_pion(1, ma_grille, (2,4))
print ma_grille
ma_grille = placer_pion(2, ma_grille, (4,3))
print ma_grille




# *** 3 *** #
print "# *** 3 *** #"


def chercher_alignement(joueur, liste, n):
	"""cherche un alignement de n symboles suivis dans une liste"""
	compteur = 1
	pions = ["O", "X"]
	for i in range(len(liste)-1):
		if liste[i] == pions[joueur-1] and liste[i] == liste[i+1]:
			compteur += 1
			if compteur >= n:
				return True
				break
		else:
			compteur = 1
	return False


# we test the function
l1 = ["O", "O", "O", "X", "X"]
print chercher_alignement(1, l1, 3)
l2 = ["O", "X", "O", "X", "X"]
print chercher_alignement(2, l2, 3)




# *** 4, 5, 6 et 7 *** #
print # *** 4, 5, 6 et 7 *** #


def generer_lignes(grille):
	"""retourne la liste des lignes d'une grille"""
	return grille


def generer_colonnes(grille):
	"""retourne la liste des colonnes d'une grille"""
	liste_colonnes = []
	# then we update them
	for i in range(len(grille)):
		liste_colonnes.append([])
		for j in range(len(grille)):
			liste_colonnes[-1].append(grille[j][i])
	return liste_colonnes


# The first diagonals are made of the indices that sum to the same values
# First diag sums to 2, second to 3, third to 4, etc., ip to N*2
def generer_diagonales1(grille):
	"""retourne la liste des diagonales d'une grille"""
	dico_diag = {} # we use a dico this time
	# the sums of the indices go from 2 to N*2
	for k in range(2, len(grille)*2+1):
		dico_diag[k] = []
	for i in range(len(grille)):
		for j in range(len(grille)):
			n = (i+1)+(j+1) # sum of the indices
			dico_diag[n].append(grille[i][j])
	return dico_diag
	

# The second diagonals are made of the indices that substract to the same values
# First diag sums to -N+1, second to -N+2, etc., up to N-1
def generer_diagonales2(grille):
	"""retourne la liste des autres diagonales d'une grille"""
	dico_diag = {} # we use a dico
	# the sums of the indices go from -N+1 to N-1
	for k in range(-len(grille)+1, len(grille)):
		dico_diag[k] = []
	for i in range(len(grille)):
		for j in range(len(grille)):
			n = (i+1)-(j+1) # difference of the indices
			dico_diag[n].append(grille[i][j])
	return dico_diag



print generer_lignes(ma_grille)
print ""
print generer_colonnes(ma_grille)
print ""
print generer_diagonales1(ma_grille)
print ""
print generer_diagonales2(ma_grille)


# *** 8 *** #
print "# *** 8 *** #"


def imprimer_grille(grille):
	for i in range(len(grille)):
		for j in range(len(grille)):
			print grille[i][j], "\t",
		print "\n"


#imprimer_grille(ma_grille)




# *** 9 *** #
print "# *** 9 *** #"


def jouer(n):
	"""simule un jeu de taille n"""
	fin_du_jeu = False
	# we generate the grid
	G = generer_grille(n)
	imprimer_grille(G)
	# each player plays a move
	while fin_du_jeu == False:
		# Player 1 plays...
		# we keep asking him to enter a position until a valid one is provided
		placement = False
		while placement == False:
			pos = input("Joueur 1: quelle position (ligne, colonne)? ")
			if G[pos[0]-1][pos[1]-1] == ".":
				G = placer_pion(1,G,pos)
				placement = True
		# we print the udated grid
		imprimer_grille(G)
		# we generate the lines, columns, digonals
		lignes = generer_lignes(G)
		colonnes = generer_colonnes(G)
		diagonales1 = generer_diagonales1(G)
		diagonales2 = generer_diagonales2(G)
		# we check if Player 1 wins
		# first in the lines...
		for l in lignes:
			if chercher_alignement(1, l, 4):
				print "Player 1 wins!"
				fin_du_jeu = True
				break # breaks the for loop
		# if not in the lines, in the columns
		if fin_du_jeu == False:
			for c in colonnes:
				if chercher_alignement(1, c, 4):
					print "Player 1 wins!"
					fin_du_jeu = True
					break # breaks the for loop
		# if not in the columns, in the diagonals of type 1
		if fin_du_jeu == False:
			for d in diagonales1.values():
				if chercher_alignement(1, d, 4):
					print "Player 1 wins!"
					fin_du_jeu = True
					break # breaks the for loop
		# if not in the diagonals of type 1, in the diagonals of type 2
		if fin_du_jeu == False:
			for d in diagonales2.values():
				if chercher_alignement(1, d, 4):
					print "Player 1 wins!"
					fin_du_jeu = True
					break # breaks the for loop
		# If player 1 hasn't won, player 2 might play
		if fin_du_jeu == False:
			# we keep asking him to enter a position until a valid one is provided
			placement = False
			while placement == False:
				pos = input("Joueur 2: quelle position (ligne, colonne)? ")
				pos = list(pos)
				if G[pos[0]-1][pos[1]-1] == ".":
					G = placer_pion(2,G,pos)
					placement = True
			imprimer_grille(G)
			# we check if 2 wins
			lignes = generer_lignes(G)
			colonnes = generer_colonnes(G)
			diagonales1 = generer_diagonales1(G)
			diagonales2 = generer_diagonales2(G)
			# first in the lines...
			for l in lignes:
				if chercher_alignement(2, l, 4):
					print "Player 2 wins!"
					fin_du_jeu = True
					break # breaks the for loop
			# if not in the lines, in the columns
			if fin_du_jeu == False:
				for c in colonnes:
					if chercher_alignement(2, c, 4):
						print "Player 2 wins!"
						fin_du_jeu = True
						break # breaks the for loop
			# if not in the columns, in the diagonals of type 1
			if fin_du_jeu == False:
				for d in diagonales1.values():
					if chercher_alignement(1, d, 4):
						print "Player 2 wins!"
						fin_du_jeu = True
						break # breaks the for loop
			# if not in the diagonals of type 1, in the diagonals of type 2
			if fin_du_jeu == False:
				for d in diagonales2.values():
					if chercher_alignement(1, d, 4):
						print "Player 2 wins!"
						fin_du_jeu = True
						break # breaks the for loop


jouer(8)


# catch exceptions (out of grid moves)...