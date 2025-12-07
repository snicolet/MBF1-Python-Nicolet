import random

couleurs = ["trefle", "carreau",  "coeur", "pique"]
hauteurs = ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]

article = ["le "] * 13
article[0]  = "l'"     # l'as
article[11] = "la "    # la dame

def couleur(carte) :
    for s in carte.split() :
        if s in couleurs :
            return couleurs.index(s)
    return None

def hauteur(carte) :
    for s in article :
        carte = carte.replace(s, " ")
    for s in carte.split() :
        if s in hauteurs :
            return hauteurs.index(s)
    return None

def numero(carte) :
    return 13 * couleur(carte) + hauteur(carte)

def carte(numero) :
    return article[numero % 13] + hauteurs[numero % 13] + " de " + couleurs[numero // 13]
    
def entree(prompt) :
    print()
    while True :
       carte = input(prompt)
       h = hauteur(carte)
       c = couleur(carte)
       if h != None and c != None :
           return carte
       print("je n'ai pas compris, recommencez svp...")

def simulate(jeu, position) :
    n = len(jeu)
    
    # a-t-on fait le tour complet ?
    if position >= n :
       position = position % n
       return carte(jeu[position])
    
    # on avance dans le jeu
    # print(carte(jeu[position]), " ====> ")
    delta = hauteur(carte(jeu[position])) + 1
    if delta > 10 :   # valet, dame, roi
       delta = 1
    position += delta
    
    return simulate(jeu, position)
    


def magie() :
    jeu = []
    for x in range(52) :
       h = hauteur(carte(x))
       if True or 0 <= h <= 5 :
          jeu.append(x)
    
    #jeu = jeu + jeu
    print('longueur du jeu = ',len(jeu))

    
    for i in range(len(jeu)) :
       break
       print(carte(jeu[i]))
    
    nb_departs = 10      # nb de departs differents à chaque tour de magie
    n          = 1000    # nb de simulations
    
    
    for nb_departs in range(1, 50) :
    
      ratage = 0
      for compteur in range(1,n+1) :
        random.shuffle(jeu)
        previous = simulate(jeu, 0)
        
        for depart in range(0, nb_departs) : 
            c = simulate(jeu, depart)
            #print(compteur,depart, " la carte sur laquelle on arrive est", c)
            if c != previous :
                # print("oops, le tour est raté")
                ratage += 1
                break
        
        reussite = compteur - ratage
    
        if compteur % n == 0 :
            print("{} nb_departs={} reussite={}".format(compteur, nb_departs, reussite / compteur))
    
    return

# programme principal

magie()


# print(couleurs)
# print(hauteurs)
# print(couleur("as de pique"))
# for i in range(len(couleurs)) :
#    msg = "{} ==> {}".format(couleurs[i] , i)
#    print(msg)
# for i in range(0,52) :
#    msg = "{} ==> {}".format(i, carte(i))
#    print(msg)
#    
# while True :
#    print("===========================================================")
#    s = input("saisir une carte : ")
#    h = hauteur(s)
#    c = couleur(s)
#    
#    if h == None or c == None :
#       break
#       
#    msg = "vous avez tape {}".format(carte(numero(s)))
#    print(msg)
#    
#    msg = "{} de {} correspond au couple (h,c) = ({},{})".format(hauteurs[h], couleurs[c], h, c)
#    print(msg)
#    
#    msg = "son numero est {}".format(numero(s))
#    print(msg)
   
   
   
   
   
