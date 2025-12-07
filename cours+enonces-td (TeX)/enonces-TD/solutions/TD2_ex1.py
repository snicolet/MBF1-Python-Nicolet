#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


#import urllib2
#response = urllib2.urlopen('http://python.org/')
#html = response.read()

#print type(html)
#print html


# *** 1 *** #
print("# *** 1 *** #")

c = "X44bf38j23jdjgfjh737nei47"


# *** 2 *** #
print("# *** 2 *** #")

c_alpha, c_num = "", ""
for x in c:
	if x.isalpha():
		c_alpha = c_alpha + x
	else:
		c_num = c_num + x

print(c_alpha)
print(c_num)


# *** 3 *** #
print("# *** 3 *** #")

if c.find("j23") != 1:
	c = c.replace("j23","j24")


# *** 4 *** #
print("# *** 4 *** #")

i1 = c.find("f")
i2 = c.find("3")
i3 = c.find("7")
#print i1, i2, i3

if (i1 < i2) and (i2 < i3) and (i1 != -1):
	print("Le pattern f37 existe dans la chaîne c")
else:
	print("Le pattern f37 n'existe pas dans la chaîne c")




