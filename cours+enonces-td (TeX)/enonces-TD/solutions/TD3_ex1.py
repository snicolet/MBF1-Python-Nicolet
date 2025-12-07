#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 *** #
print "# *** 1 *** #"

n = input("Entrer un nombre: ")
for i in range(1,11):
	print n*i


# *** 2 *** #
print "# *** 2 *** #"

n = input("Entrer un nombre: ")
for i in range(1,11):
	print n*i,


# *** 3 *** #
print "\n"
print "# *** 3 *** #"

n = input("Entrer un nombre: ")
for i in range(n):
	print "Table de", i+1, ":",
	for j in range(1,11):
		print (i+1)*j,
	print "\n"


# *** 4 *** #
print "\n"
print "# *** 4 *** #"

n = input("Entrer un nombre: ")
for i in range(n):
	print "*"*(i+1)
	
	
# *** 5 *** #
print "# *** 5 *** #"

n = input("Entrer un nombre: ")
for i in range(n):
	print " "*((n-1)-i) + ("* "*(i+1))[:2*(i+1)-1] + " "*((n-1)-i)
