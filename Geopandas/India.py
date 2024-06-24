# %%
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fiona as fn

# %%

in_st = r'Indian_states.shx'
in_st

# %%
gdf  =gpd.read_file(in_st)
gdf.head()
gdf.geom_type

# %%
gdf.plot()

# %%
in_b = r'India_boundary.shx'
gdf1  =gpd.read_file(in_b)
gdf1.head()
gdf1.plot()

# %%
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the shapefile
india_map = gpd.read_file("Indian_states.shx")

# Load the CSV file with state capitals
capitals = pd.read_csv("State_capitals.csv")

# Create a GeoDataFrame for the capitals
capitals_gdf = gpd.GeoDataFrame(capitals, geometry=gpd.points_from_xy(capitals.Longitude, capitals.Latitude))

# Plot the map
fig, ax = plt.subplots(figsize=(15, 15))
india_map.plot(ax=ax, color='white', edgecolor='black')

# Plot the state capitals
capitals_gdf.plot(ax=ax, color='red', markersize=50, label='State Capital')

# Annotate state capitals
for idx, row in capitals_gdf.iterrows():
    ax.annotate(text=row['Capital'], xy=(row['Longitude'], row['Latitude']), xytext=(3, 3),
                textcoords="offset points", fontsize=12, color='blue')

# Draw lines connecting capitals (example: creating a simple network)
for i in range(len(capitals_gdf) - 1):
    for j in range(i + 1, len(capitals_gdf)):
        x = [capitals_gdf.iloc[i].geometry.x, capitals_gdf.iloc[j].geometry.x]
        y = [capitals_gdf.iloc[i].geometry.y, capitals_gdf.iloc[j].geometry.y]
        ax.plot(x, y, color='green', linewidth=1)

# Set title and show legend
plt.title('Map of India with State Capitals')
plt.legend()
plt.show()


# %%
len(capitals_gdf)

# %%
##Enhanced visualization code
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the shapefile
india_map = gpd.read_file("Indian_states.shx")

# Load the CSV file with state capitals
capitals = pd.read_csv("State_capitals.csv")

# Create a GeoDataFrame for the capitals
capitals_gdf = gpd.GeoDataFrame(capitals, geometry=gpd.points_from_xy(capitals.Longitude, capitals.Latitude))

# Plot the map
fig, ax = plt.subplots(figsize=(10, 10))
india_map.plot(ax=ax, color='lightgrey', edgecolor='black', linewidth=0.5)

# Plot the state capitals
capitals_gdf.plot(ax=ax, color='red', markersize=100, marker='o', label='State Capital')

# Annotate state capitals with state names
for idx, row in capitals_gdf.iterrows():
    ax.annotate(
        text=f"{row['State']}\n({row['Capital']})",
        xy=(row['Longitude'], row['Latitude']),
        xytext=(3, 3),
        textcoords="offset points", ##slightly offset annotations for better readability
        fontsize=10,
        color='blue',
        weight='bold',
        ha='right',
        va='top'
    )

# Draw lines connecting capitals
for i in range(len(capitals_gdf) - 1):
    for j in range(i + 1, len(capitals_gdf)):
        x = [capitals_gdf.iloc[i].geometry.x, capitals_gdf.iloc[j].geometry.x]
        y = [capitals_gdf.iloc[i].geometry.y, capitals_gdf.iloc[j].geometry.y]
        ax.plot(x, y, color='green', linewidth=0.8, linestyle='dotted', alpha=0.6)
        #alpha connecting lines are slightly transparent

# Additional customization
plt.title('Map of India with State Capitals', fontsize=20, weight='bold')
plt.xlabel('Longitude', fontsize=15)
plt.ylabel('Latitude', fontsize=15)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=12)

# Adjust plot limits
plt.xlim([68, 98])
plt.ylim([6, 38])

# Save the plot as an image
plt.savefig('india_state_capitals.png', dpi=300, bbox_inches='tight')
#dpi = Dots per inch, high resolution output, you can change .png to .pdf or.jpg
# Show the plot
plt.show()


# %%
pip install numpy>1.0.0 wheel setuptools>=67


# %%
pip install gdal[numpy]=="$(gdal-config --version).*"

# %%
pip install osego


# %%
# import the GeoPandas libraries
import gdal
import geopandas
import geopandas as gpd

# import numpy and scipy
import numpy as np
from scipy import ndimage
import matplotlib.pylab as pylab
import matplotlib.pyplot as pyplot

# load a couple of shapefiles
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

# print the first few features of the file
print(world.head())

# GeoDataFrames are organized as named columns and then indexed arrays
# so this gets the number of entries in the 'name' column.
NumFeatures=len(world.name)

# access the attributes in the file to print all names
Count=0
while (Count<NumFeatures):
	print(world.name[Count])
	Count+=1

# print the bounds of the entire world
print(world.bounds)

# remove Antarctica from the world shapefile and then project it
world = world[(world.name != "Antarctica") & (world.name != "Fr. S. Antarctic Lands")]
world = world.to_crs({'init': 'epsg:3395'}) # world.to_crs(epsg=3395) would also work

world.plot() # create a map

pyplot.show() # show the map

print(world.crs)

# plot by GDP per cap

world = world[(world.pop_est>0) & (world.name!="Antarctica")]

world['gdp_per_cap'] = world.gdp_md_est / world.pop_est

world.plot(column='gdp_per_cap')

pyplot.show()

# %%
