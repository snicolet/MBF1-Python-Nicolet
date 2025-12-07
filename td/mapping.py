import geopandas
import pandas as pd
import matplotlib.pyplot as plt

from geodatasets import get_path


world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))

path = get_path("naturalearth.land")
land = geopandas.read_file(path)

print( world.head())
print(world)

fig, ax = plt.subplots(figsize=(16, 10))
world.plot(color="lightgrey", ax=ax)

# creation des limites des axes
plt.xlim([-180, 180])
plt.ylim([-90, 90])
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# titre
plt.title("carte du monde")

# affichage de la carte
plt.show()