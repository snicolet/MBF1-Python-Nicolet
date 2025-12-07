import numpy as np
import matplotlib.pyplot as plt
#plt.style.use("seaborn")
plt.rcParams.update({'font.family':'serif'})

import math

print("hello")


def creer_brownien(precision) :
    ''' renvoie un tableau numpy de taille precision contenant un mouvement brownien sur [0..1] '''

    n = precision
    
    delta = np.random.normal(0.0 , 1.0, n)
    w     = np.zeros(n)
    
    # on calcule les somme partielles des deplacements elementaires
    for k in range(1, len(w)) :
       # w[k] = delta[k]            # bruit blanc
       w[k] = w[k-1] + delta[k]     # brownien = integrale du bruit blanc
       
    
    # on normalise pour obtenir une variance de 1.0
    for k in range(0, len(w)) :
       w[k] = w[k] / math.sqrt(n)
    
    return w


def creer_brownien_generalise(precision, a, b) :
    ''' renvoie le brownien de variation dX = a.dt + b.dW '''
    n      = precision
    w      = creer_brownien(n)
    result = np.zeros(n)
    for k in range(0, n) :
        t = k / n
        result[k] = a * t + b * w[k]
    return result


def evaluer_brownien(X, t) :
    ''' evalue X à la date t, où t est dans [0..1] '''
    n = len(X) - 1
    i = int(t * n)
    return X[i]


def transformer_brownien(f, X) :
    ''' renvoie Y = f(X) '''
    n = len(X)
    result = []
    for k in range(0, n) :
        t = k / n
        result.append( f(t, X[k]) )
    return result

def f(t, X) :
    return X ** 2 + 20

def creer_graphique() :

    precision = 10000
    dates     = np.linspace(0.0, 1.0, num=precision)

    p = 100    # nombre de courbes
    a = 10.0   # tendance
    b = 2.0    # volatibilite


    
    
    # creation des series de mouvements browniens
    courbes_X = []
    courbes_Y = []
    for num in range(0, p) :
        X = creer_brownien_generalise(precision, a, b)
        Y = transformer_brownien(f, X)
        courbes_X.append(X)
        courbes_Y.append(Y)

    # moyenne
    moyenne = []
    for k in range(0, precision) :
        somme = 0
        for num in range(0,p) :
            somme = somme + courbes_Y[num][k]
        moyenne.append(somme / p)


    # creation des graphiques
    fig, ax1 = plt.subplots(nrows = 1)
    fig.set_size_inches(10, 10)
    

    ax1.set_title("exemples de mouvements browniens")
    ax1.set_xlabel("temps")
    ax1.set_ylabel("valeur")
    for num in range(0,p) :
       ax1.plot(dates,  courbes_X[num], linewidth=0.5, label="", alpha=0.3)
       ax1.plot(dates,  courbes_Y[num], linewidth=0.5, label="", alpha=0.15 )
       
    ax1.plot(dates, moyenne, linewidth=4,
                             linestyle="--",
                             color="black",
                             label="moyenne des f(X)")

    ax1.legend(loc="upper left")

    # set the spacing between subplots
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




