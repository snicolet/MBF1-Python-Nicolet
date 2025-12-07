#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


def facto(n):
	"""Fonction factorielle"""
	if n == 0:
		return 1
	else:
		return n * facto(n-1)


# Exemples:
for x in range(10):
	print facto(x)


