import numpy as np
import matplotlib.pyplot as plt


def generer(n) :
   x = np.random.uniform(-1.0 , 1.0, n)
   y = np.random.uniform(-1.0 , 1.0, n)
   return x,y


def montecarlo(liste_X, liste_Y, formule) :

  n = len(liste_X)
  fig, ax = plt.subplots()
  fig.set_size_inches(10, 10)
  
  ax.set_xlim(-1.0, 1.0)
  ax.set_ylim(-1.0, 1.0)
  
  acceptX = []
  acceptY = []
  rejectX  = []
  rejectY  = []
  
  compteur = 0
  for k in range(0, n):
  
     x = liste_X[k]
     y = liste_Y[k]
  
     accept = eval(formule)
     
     if accept :
         compteur += 1
         acceptX.append(x)
         acceptY.append(y)
     else :
         rejectX.append(x)
         rejectY.append(y)
    
     surface = 4 * compteur / (k+1)

     if k % 1000 == 0 :
        titre = "k = " + str(k) + ", surface = " + str(round(surface, 6))
        plt.title(titre)
        plt.scatter(acceptX, acceptY, color='pink', s=30)
        plt.scatter(rejectX, rejectY, color='green', s=30)
        plt.pause(0.1)
  
  plt.show()
  
  return



# programme principal

x, y = generer_points(10001)
print(x)

formule = " x**2 + y**2 <= 1.0 "
montecarlo(x, y, formule)

formule = " abs(x)**0.5 + abs(y)**0.5 <= 1.0 "
montecarlo(x ,y, formule)

formule = " abs(x)**2 + (0.3 + 1.5*y - abs(x)**0.6)**2 <= 1.0 "
montecarlo(x, y, formule)









