#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


with open("test.txt","w") as f:
	f.write("1ere ligne\n")
	f.write("2eme ligne\n")
	f.write("3eme ligne\n")
	f.write("4eme ligne\n")
	f.write("5eme ligne\n")
	
with open("test.txt","r") as f:
	contenu = f.read()
	print contenu
	
with open("test.txt","r") as f:
	l = f.readlines()
	print l[1]

with open("test.txt","a") as f:
	f.write("derniere ligne")
	
with open("test.txt","r") as f:
	l = f.readlines()
	print l[-2]