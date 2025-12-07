
couleurs = ["trefle", "carreau",  "coeur", "pique"]
hauteurs = ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]

article     = ["le "] * 13   # le 2, le 3, le valet, le roi...
article[0]  = "l'"           # l'as
article[11] = "la "          # la dame


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
    c = numero // 13
    h = numero % 13
    return article[h] + hauteurs[h] + " de " + couleurs[c]
    
    
def entree(prompt) :
    print()
    while True :
       carte = input(prompt)
       h = hauteur(carte)
       c = couleur(carte)
       if h != None and c != None :
           return carte
       print("je n'ai pas compris, recommencez svp...")
    return


def magie() :

   premiere = entree("saisir la premiere carte : ")
   a        = numero(entree("saisir la deuxieme carte : "))
   b        = numero(entree("saisir la troisieme carte : "))
   c        = numero(entree("saisir la quatrieme carte : "))

   if a < b < c :
      decalage = 1
   if a < c < b :
      decalage = 2
   if b < a < c :
      decalage = 3
   if b < c < a :
      decalage = 4
   if c < a < b :
      decalage = 5
   if c < b < a :
      decalage = 6

   c = couleur(premiere)
   h = hauteur(premiere)
      
   x = carte( c * 13 + ((h + decalage) % 13) )
   
   print("\n\n")
   print("hmm, je pense que la cinquieme carte est", x)
   print("\n\n")

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
   
   
   
   
   
