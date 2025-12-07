import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def lorenz(x, y, z, s, r, b) :
    dx = s * (y - x)
    dy = r * x - y - x * z
    dz = x * y - b * z
    return (dx, dy, dz)


def simulation(sigma, rho, beta, h, n) :
   # les tableaux numpy contenant les suites x, y et z
   x = np.empty(n+1)
   y = np.empty(n+1)
   z = np.empty(n+1)

   # valeurs initiales
   x[0] = 0.0
   y[0] = 1.0
   z[0] = 1.05

   # simulation
   for i in range(0, n) :
      dx,dy,dz = lorenz(x[i], y[i], z[i], sigma, rho, beta)
      x[i+1] = x[i] +  h * dx
      y[i+1] = y[i] +  h * dy
      z[i+1] = z[i] +  h * dz

   # on retourne les trois tableaux x, y, z
   return x, y, z


def affichage(sigma, rho, beta, x, y, z) :

    plt.figure()
    fig = plt.axes(projection='3d')

    titre = "({}, {}, {})".format(sigma, rho, beta)
    
    fig.set_title("attracteur de Lorentz " + titre)
    fig.set_xlabel("X")
    fig.set_ylabel("Y")
    fig.set_zlabel("Z")
  
    fig.plot(x,y,z, lw=0.5)
    plt.savefig(titre + ".png")
    
    return 

def attracteur(sigma, rho, beta) :
   x,y,z = simulation(sigma, rho, beta, 0.01, 10000)
   affichage(sigma, rho, beta, x, y, z)
   return


# programme principal

# intervales pour sigma, rho et beta
(s0,s1) = (10.0   , 10.0)  
(r0,r1) = (28.0   , 10.0)
(b0,b1) = (2.666  , 2.0)

# nombre de figures
n = 9

for k in range(0, n+1) :
   sigma = s0 + k * (s1 - s0) / n
   rho   = r0 + k * (r1 - r0) / n
   beta  = b0 + k * (b1 - b0) / n
   attracteur(sigma, rho, beta)

plt.show()


# peut-etre necessaire pour les versions anciennes de matplotlib :
# python3 -m poetry add matplotlib
# python3 -m poetry add seaborn
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure().gca(projection='3d')