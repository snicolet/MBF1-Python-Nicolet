#######################################
## Exercice 1 (définition de fonctions)
#######################################
       
import math

# definition d'une fonction f
def f(x) :
    return x * x

# definition d'une fonction g
def g(x) :
    return 2 * math.sqrt(1 - x * x)

print("======================================")
print(f(3))
print(f(-5))
print(f(0.01))


# calcul de l'integrale d'une fonction f sur l'intervale [a..b] 
# par la methode des rectangles avec n subdivisions.
# Source https://fr.wikipedia.org/wiki/Somme_de_Riemann
def integrale(f, a, b, n) :

    h = (b - a) / n     # largeur de chaque rectangle
    somme = 0           # somme partielle
    
    for k in range(0, n) :
        x_k = a + k * h
        somme = somme + h * f(x_k)
    
    return somme


print()
print(integrale(g, -1, 1, 2))
print(integrale(g, -1, 1, 10))
print(integrale(g, -1, 1, 100))
print(integrale(g, -1, 1, 1000))
print(integrale(g, -1, 1, 10000))
print(integrale(g, -1, 1, 100000))


########################################
## Exercice 2 (transposée d'une matrice)
########################################

A = [[1, 2], [3, 4], [5, 6]]

n = len(A)
m = len(A[0])

print("======================================")
print("A = ", A)
print("A est une matrice de taille (", n, ",", m ,")")


# calcul de la transposee C de A
print("C est une matrice de taille (", m, ",", n ,")")
C = [[0 for j in range(n)] for i in range(m)]
    
for i in range(m) :
    for j in range(n) :
        C[i][j] = A[j][i]

print("C = ", C)


###############################
## Exercice 3 (carrés magiques)
###############################

## Source : https://fr.wikipedia.org/wiki/Carré_magique_(mathématiques)

# carré magique de Luo Shu
luo = [[4, 9, 2] , 
       [3, 5, 7] , 
       [8, 1, 6]]

# carré magique de Dürer
durer = [[16,  3,  2, 13] ,
         [ 5, 10, 11,  8] ,
         [ 9,  6,  7, 12] ,
         [ 4, 15, 14,  1]]

m = luo  # ou bien m = durer
n = len(m)

print("======================================")
print(m)
print(n)


# verifions que m est un carré magique

for i in range(0, n) :
    S = 0
    for k in range(0, n) :
        S = S + m[i][k]
    print("ligne", i,  " la somme vaut", S)

for i in range(0, n) :
    S = 0
    for k in range(0, n) :
        S = S + m[k][i]
    print("colonne", i,  " la somme vaut", S)

S = 0
for k in range(0, n) :
   S = S + m[k][k]
print("diagonale principale   la somme vaut", S)

S = 0
for k in range(0, n) :
   S = S + m[k][n-1-k]
print("diagonale secondaire   la somme vaut", S)


# pour verifier que tous les elements sont distincts,
# le plus simple est de mettre tous les elements dans
# un seul tableau, de trier ce tableau puis de parcourir
# la tableau trie en cherchant des doublons

t = []
for i in range(0,n) :
   for k in range(0,n) :
      t.append(m[i][k])

u = sorted(t)

for i in range(0, n * n - 1) :
   if u[i] == u[i+1] :
       print("élément dupliqué :", u[i])
    


##########################################
## Exercice 4 (multiplication matricielle)
##########################################

A = [[7, 8], [9, 10], [11, 12]]
B = [[1, 2, 3], [4, 5, 6]]       # ou bien B = A

n = len(A)
m = len(A[0])
p = len(B)
q = len(B[0])

print("======================================")
print("A = ", A)
print("B = ", B)
print("A est une matrice de taille (", n, ",", m ,")")
print("B est une matrice de taille (", p, ",", q ,")")


# calcul du produit matriciel C = AB
if m != p :
    print("les dimensions sont incompatibles")
    C = []
else :
    print("C est une matrice de taille (", n, ",", q ,")")
    C = [[0 for j in range(q)] for i in range(n)]
    
    for i in range(n) :
        for j in range(q) :
            C[i][j] = 0
            for k in range(m) :
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

print()
print("C = ", C)
print()






























