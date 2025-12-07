#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


def fibonacci(n):
	"""Suite de Fibonacci"""
	if n == 0 or n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)


# Exemple:
for x in range(10):
	print fibonacci(x)


