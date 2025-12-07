#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 et 2 *** #
print "# *** 1 et 2 *** #"


from math import pi

def surf_cercle(r = 1):
	return pi*r**2
	
print surf_cercle(3)
print surf_cercle()



# *** 3 et 4 *** #
print "# *** 3 et 4 *** #"


def vol_boite(x1 = -1, x2 = -1, x3 = -1):
	if x1 != -1 and x2 == -1 and x3 == -1: # un argument fourni
		return x1**3
	elif x1 != -1 and x2 != -1 and x3 == -1: # deux arguments fournis
		return x1*x1*x2
	elif x1 != -1 and x2 != -1 and x3 != -1: # trois arguments fournis
		return x1*x2*x3

print vol_boite(1.7, 8.42, 5.48)
print vol_boite(x1 = 2.0)
print vol_boite(x1 = 2.0, x2 = 3)
print vol_boite(x1 = 1.7, x2 = 8.42, x3 = 5.48)



# *** 5 et 6 *** #
print "# *** 5 et 6 *** #"


def remplacement(c1 = " ", c2 = "*", ch = ""):
	ch2 = ""
	for i in range(len(ch)):
		if ch[i] == c1:
			ch2 = ch2 + c2
		else:
			ch2 = ch2 + ch[i]
	return ch2
		

print remplacement(".", "!", "Bonjour.")
print remplacement(ch = "Dans ce cas, les deux premiers arguments ne sont pas specifies...")


