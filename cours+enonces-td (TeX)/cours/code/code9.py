# -*- coding: utf-8 -*-

# ouverture/création en mode écriture, puis fermeture
f1 = open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","w")
f1.close()

# ouverture en mode lecture puis fermeture
f1 = open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","r")
f1.close()

# ouverture/création en mode écriture, puis fermeture
with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","w") as f1:
	pass

# création et écriture
with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","w") as f1:
	f1.write("1ere ligne\n") # \n code un retour de ligne
	f1.write("2eme ligne\n")
	f1.write("3eme ligne\n")

# lecture
with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","r") as f1:
	x = f1.read(5)
	print(x)
	y = f1.readline()
	print(y)
	z = f1.readlines()
	print(z)
	
# À chaque réouverture, le curseur se replace au début
with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","r") as f1:
	x = f1.read()
	print(x)

with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","r") as f1:
	for x in f1:
		print(x)

with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","r") as f1:
	for l in f1.readlines():
		print(l)
		
print("")
 
# création et écriture d'un fichier à accès direct
with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","w+") as f2:
	f2.write("1ere ligne bis\n") # \n code un retour de ligne
	f2.write("2eme ligne bis\n")
	f2.write("3eme ligne bis\n")

# lecture d'un fichier à accès direct
with open("/Users/jcabessa/Desktop/MAIN/Courses/PYTHON/2016_Paris/fichier1.txt","r+") as f2:
	f2.seek(8)
	x = f2.read()
	print(x)