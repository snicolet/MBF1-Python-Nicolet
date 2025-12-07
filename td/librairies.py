
# installation de librairies ?
# dans une invite de commande MS-DOS ou un Terminal Mac, taper :

# python -m pip install yfinance
# python -m pip install numpy
# python -m pip install pandas

import yfinance as yf
import numpy    as np
import matplotlib.pyplot as plt
import pandas   as pd

print("hello")

# exemple : importation du cours du DAX (=CAC40 allemand)
dax = yf.download('^GDAXI', start="2022-01-01", end="2023-01-01")
print(dax)

# sauvegarde dans un fichier CSV
dax.to_csv("dax.csv")

# trace de courbe
y = dax["Open"]

fig, ax = plt.subplots()
ax.set_title("Evolution du DAX en 2022")
plt.plot(y)
plt.show()


print("j'ai fini")



