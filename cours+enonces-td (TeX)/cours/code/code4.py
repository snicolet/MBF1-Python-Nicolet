# -*- coding: utf-8 -*-

s = "Hello"
print(type(s))

print("")

a = "Bonnie"
b = "Clyde"
print(a + " & " + b)
print(a*3)

print("")

a = "bonjour"
print(a[0])
print(a[1])
print(a[2])
print(a[6])
print(a[-1])
print(a[-2])
print(a[0:2])
print(a[2:7])
print(a[3:4])

print("")

s = "TIGRE"
print(s.lower())
print(s) # donc s n'est pas modifiée!
t = s.lower()
print(t) # t est une nouvelle liste créée à partit de s
print(s.replace("G","T"))
print(s) # s n'est pas modifiée!

print("")

a = "bonjour"
print(len(a))

print("")

s = "TIGRE"
for c in s:
	print(c)

print("")

# phrase = input("Entrer une phrase: ")
# # transforme les maj. en min.
# phrase = phrase.lower()
# # enleve les espaces
# phrase = phrase.replace(" ", "")
# 
# print(phrase)
# 
# palindrome = True # la var bool palindrome donnera la réponse...
# g = 0           	# indice 1er caractere de la liste
# d = len(phrase) - 1 # indice dernier caractere de la liste
# 
# while g < d:
#     if phrase[g] != phrase[d]:
#         palindrome = False
#         break
#     else:
# 	    g = g + 1
# 	    d = d - 1
#     
# if palindrome == True:
# 	print("C'est un palindrome")
# else:
# 	print("Ce n'est pas un palindrome")

l = [1,2,3.5,"bonjour",True]
print(l)
print(type(l))

print("")

fruits = ['orange', 'banane', 'pomme', 'cerise']
print(len(fruits))
print(fruits[0])
print(fruits[-1])
print(fruits[-2])
print(fruits[1:3])
print(fruits[len(fruits)-1])

print("")

l = ["jaune","orange","rouge","vert","bleu"]
l[0] = "jaune pale"
print(l)
l[-1] = "bleu fonce"
print(l)
l[2:4] = ["rouge vif","vert clair"]
print(l)

print("")

l = ["jaune","orange","rouge"]
l.append(2.83)
print(l)
print(l.count("rouge"))
l.extend([1,2,3])
print(l)
print(l.index("rouge"))
l.insert(2,True)
print(l)
l.pop(3)
print(l)
l.remove("jaune")
print(l)
l.reverse()
print(l)

print("")

l = [1,2,"monday",3,4,5,"tuesday",6,7,8,9,10]
for x in l:
	if isinstance(x, str):
		print(x)
	else:
		pass

print("")

l = [1,2,3,[4,5,6]]
print(l[3])
print(l[3][0])
print(l[3][1])
print(l[3][2])

print("")

v1 = [2.34, 4.35, 6.18]
v2 = [-3.74, 7.39, 18.96]
v3 = [2.34, 12.83, -26.47]
m = [v1, v2, v3]
print(m)
print(m[1][2])

print("")

for i in range(0,1000):
	if i%27 == 0:
		print(i)
		
print("")

t = (1,2,3)
print(type(t))

print("")

t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)
#t1[2] = "bonjour"

print("")

identifiant = [("James","Dean"), "Université P2", "M1"]
identifiant[1] = "Université Paris 6"
identifiant[2] = "M2"
print(identifiant)
identifiant[0] = ("James","Bond")

print("")

d = {"Alice": 4328, "Bob": 4357, "Carmen": 4392}
print(type(d))
print(d)
print(d["Bob"])
d["Dan"] = 4367
print(d)
del d["Dan"]
print(d)
d["Alice"] = 1234
print(d)
print("Alice" in d)
print("Anna" in d)
print("Anna" not in d)


print("")

d = {"Alice": 4328, "Bob": 4357, "Carmen": 4392}
print(d.get("Alice"))
print(d.keys())
print(d.values())
d2 = d.copy()
print(d2)
d.clear()
print(d)

my_dico = {"Person1": ["Alice",2308,"M1"], "Person2": ["Bob",3407,"L3"], "Person3": ["Carmen", 3276,"M2"]}
for k in my_dico.keys():
	print(k,my_dico[k])

print("")

print(int("2"))
print(float("2.34"))
print(str(18))
print(str(7.56))
print(str([1,2,3]))

