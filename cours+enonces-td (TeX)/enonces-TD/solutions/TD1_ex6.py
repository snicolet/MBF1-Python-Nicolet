#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


t = input("Entrer la temperature: ")
print(str(t) + "C" " = " + str(9.0/5.0*t + 32) + "F")
print(str(t) + "F" " = " + str(5.0/9.0*(t - 32)) + "C")