import numpy as np
import matplotlib.pyplot as plt

# plt.style.use("seaborn")
# plt.rcParams.update({'font.family':'serif'})

import math

print("hello")


def creer_brownien(precision) :
    ''' renvoie un tableau numpy de taille precision contenant un mouvement brownien sur [0..1] '''

    n = precision
    
    delta = np.random.normal(0.0 , 1.0, n)
    w     = np.zeros(n)
    
    # on calcule les sommes partielles des deplacements elementaires
    for k in range(1, len(w)) :
       # w[k] = delta[k]             # bruit blanc
       w[k] = w[k-1] + delta[k]     # brownien = integrale du bruit blanc
       
    
    # on normalise pour obtenir une variance de 1.0
    for k in range(0, len(w)) :
       w[k] = w[k] / math.sqrt(n)
    
    return w


def evaluer_brownien(b, t) :
    ''' evalue b à la date t, où t est dans [0..1] '''
    n = len(b) - 1
    i = int(t * n)
    return b[i]


def creer_graphique() :

    # nombre de points
    precision = 10000
    
    # on tracera nos mouvements browniens sur [0..1]
    dates  = np.linspace(0.0, 1.0, num=precision)
    
    # creation des series de mouvements browniens
    w  = creer_brownien(precision)
    w1 = creer_brownien(precision)
    w2 = creer_brownien(precision)
    w3 = creer_brownien(precision)


    # creation des graphiques
    fig, (ax1,ax2) = plt.subplots(nrows = 2)
    fig.set_size_inches(10, 10)
    

    ax1.set_title("exemples de mouvements browniens")
    ax1.set_xlabel("temps")
    ax1.set_ylabel("valeur")
    ax1.plot(dates,  w, linewidth=0.5, label="w" )
    ax1.plot(dates, w1, linewidth=0.5, label="w1")
    ax1.plot(dates, w2, linewidth=0.5, label="w2")
    ax1.plot(dates, w3, linewidth=0.5, label="w3")
    ax1.legend(loc="lower left")


    ax2.set_title("histogramme de w,w1")
    ax2.hist(w , bins=1000, alpha=0.7)
    ax2.hist(w1, bins=1000, alpha=0.7)

    # ajustons l'espace entre nos deux graphiques
    plt.subplots_adjust(left=0.1,
                    bottom=0.05, 
                    right=0.9, 
                    top=0.95, 
                    wspace=0.1, 
                    hspace=0.3)

    plt.show()
    return



# programme principal

creer_graphique()





