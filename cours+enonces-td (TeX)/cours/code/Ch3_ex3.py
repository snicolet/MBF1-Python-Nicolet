#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


name = input("Name? ")
password = input("Password? ")

if name == "Dan" and password == "123456":
	print("Welcome...")
else:
	print("Acess denied.")
