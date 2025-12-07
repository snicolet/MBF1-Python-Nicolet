import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import
df = pd.read_csv("diamonds.csv")
print(df)

# extraction des colonnes (le prix)
p = df["price"]
print(p)
print(p.describe())
moyenne = p.mean()
variance = p.var()
ecart_type = p.std()

# transformation d'une colonne
p2 = p * 1.3 + 5
print(p2)

# nuage de points avec matplotlib
x = df["carat"]
y = df["price"]
fig, ax = plt.subplots()
plt.scatter(x, y, s=1, alpha=0.2)
plt.show()

# pd.plotting.scatter_matrix(df, alpha=0.2)

# tri selon le nombre de carats
df = df.sort_values("carat", ascending=False)
print(df)

# extraction des lignes (enregistrements)
a = df[ df.cut == "Ideal" ]
b = df[ df.cut == "Fair" ]
c = df[ df.cut == "Premium" ]
d = df[ df.cut == "Good" ]
e = df[ df.cut == "Very Good" ]

print(a)
print(b)
print(c)
print(d)
print(e)

a.to_csv("ideal.csv", index=False)

# lecture du fichier AnomalieTempe_RCP2.6_mensuel.txt
#df = pd.read_csv("AnomalieTempe_RCP2.6_mensuel.txt")
#print(df)

# lecture du fichier anomalie.txt
df = pd.read_csv("anomalie.txt")
print(df)

df = pd.read_csv("anomalie.txt", sep=";", comment="#", skip_blank_lines=True)
print(df)







