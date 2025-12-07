#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line

def DecimalToBinary(n):
	if n == 0:
		res = str(0)
	else:
		res = "" # chaine vide
	while n != 0:
		res = str(n % 2) + res
		n = n / 2 # division entiere
	return res

# Exemple (faire demo):
print DecimalToBinary(26)
print DecimalToBinary(45)
print DecimalToBinary(267)


def DecimalToBinaryRec(n):
	if n > 0:
		return DecimalToBinaryRec(n / 2) + str(n % 2)
	else:
		return ""

# Exemple (faire demo):
print DecimalToBinaryRec(26)
print DecimalToBinaryRec(45)
print DecimalToBinaryRec(267)
