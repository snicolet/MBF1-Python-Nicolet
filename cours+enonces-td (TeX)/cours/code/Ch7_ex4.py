#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line



def Hanoi(n, p1, p3, p2):
	if n > 0 :
		Hanoi(n-1, p1, p2, p3)
		print "Bouger le disque de " + str(p1) + " vers " + str(p3)
		Hanoi(n-1, p2, p3, p1)
	else:
		pass

# Exemple:
#Hanoi(7, 1 ,3 ,2)



# *** AMELIORATION AVEC GRAPHISME *** #


# liste des piliers...
# chaque pilier est une liste de nombres
# au début, le pilier 1 est rempli et les deux autres vides
piliers = [[7,6,5,4,3,2,1], [], []]

def bouger_disque(p1,p2):
	print "\n"
	print "Bouger le disque de " + str(p1) + " vers " + str(p2)
	# mise a jour des piliers
	piliers[p2-1].append(piliers[p1-1].pop())
	# impression des piliers (dans le cas n=7)
	for i in range(7):
		print "" # pour aller a la ligne
		for p in piliers:
			# on complete le pilier avec des points
			p_mod = p + ["."]*(7-len(p))
			# on les imprime depuis la fin vers le debut
			# pour avoir le petits disques en dessus
			# et les gros en dessous
			print p_mod[-i-1], "   ",

#bouger_disque(1, 2)
#bouger_disque(1, 3)
#bouger_disque(2, 3)
		
def Hanoi_bis(n, p1, p3, p2):
	if n > 0 :
		Hanoi_bis(n-1, p1, p2, p3)
		bouger_disque(p1,p3) # appel nouvelle fonction
		Hanoi_bis(n-1, p2, p3, p1)
	else:
		pass

# Exemple:
Hanoi_bis(7, 1 ,3 ,2)

