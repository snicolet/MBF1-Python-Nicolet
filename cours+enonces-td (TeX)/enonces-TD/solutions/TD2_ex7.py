#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it accordingly.

# The second line is the utf-8 encoding line



# *** 1 *** #
print "# *** 1 *** #"

dico_fr_ang = {"bonjour" : "Hello", "au revoir" : "bye"}
print dico_fr_ang


# *** 2 *** #
print "# *** 3 *** #"
dico_fr_ang["cerveau"] = "brain"
print dico_fr_ang


# *** 3 *** #
print "# *** 3 *** #"

for x in dico_fr_ang.keys():
	if x == "cerveau":
		print "la traduction anglaise de", x, "est", dico_fr_ang[x]


# *** 4 *** #
print "# *** 4 *** #"

dico_ang_fr = {}
for k, v in dico_fr_ang.items():
	dico_ang_fr[v] = k
print dico_ang_fr


# *** 5 *** #
print "# *** 5 *** #"

for x in dico_ang_fr.keys():
	if x == "brain":
		print "la traduction francaise de", x, "est", dico_ang_fr[x]


# *** 6 *** #
print "# *** 6 *** #"

for k, v in dico_ang_fr.items():
	if v == "cerveau":
		print k


# *** 7 *** #
print "# *** 7 *** #"

dico_fr_ang = {"bonjour" : ["Hello", "Hi"], "au revoir" : ["bye", "bye bye"]}
dico_fr_ang["chemin"] = ["path", "way"]
print dico_fr_ang

# *** 8 *** #
print "# *** 8 *** #"

print dico_fr_ang["chemin"][1] # second element of ["path", "way"]
