# %%
"""
*This code explains how to conver pandas dataframe into geoDataFrame*
"""

# %%
#pip install geodatasets


# %%
import pandas as pd
import geopandas
import matplotlib.pyplot as plt
#from geodatasets import get_path

# %%
df = pd.DataFrame(
    {
        "City": ["Buenos Aires", "Brasilia", "Santiago", "Bogota", "Caracas"],
        "Country": ["Argentina", "Brazil", "Chile", "Colombia", "Venezuela"],
        "Latitude": [-34.58, -15.78, -33.45, 4.60, 10.48],
        "Longitude": [-58.66, -47.91, -70.66, -74.08, -66.86],
    }
)

gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
)

gdf.head()


# %%
world = geopandas.read_file(get_path("naturalearth.land"))

# We restrict to South America.
ax = world.clip([-90, -55, -25, 15]).plot(color="white", edgecolor="black")

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax, color="red")

plt.show()

# %%
## if DataFrame having points in WKT format
df = pd.DataFrame(
    {
        "City": ["Buenos Aires", "Brasilia", "Santiago", "Bogota", "Caracas"],
        "Country": ["Argentina", "Brazil", "Chile", "Colombia", "Venezuela"],
        "Coordinates": [
            "POINT(-58.66 -34.58)",
            "POINT(-47.91 -15.78)",
            "POINT(-70.66 -33.45)",
            "POINT(-74.08 4.60)",
            "POINT(-66.86 10.48)",
        ],
    }
)
from shapely import wkt

df["Coordinates"] = geopandas.GeoSeries.from_wkt(df["Coordinates"])

gdf = geopandas.GeoDataFrame(df, geometry="Coordinates")

print(gdf.head())
ax = world.clip([-90, -55, -25, 15]).plot(color="white", edgecolor="black")

gdf.plot(ax=ax, color="red")

plt.show()


# %%
"""
**Analysis of raster data**
"""

# %%

#pip install rasterio


# %%
import geopandas
import rasterio
import matplotlib.pyplot as plt
from shapely.geometry import Point

# %%
# Create sampling points
points = [
    Point(625466, 5621289),
    Point(626082, 5621627),
    Point(627116, 5621680),
    Point(625095, 5622358),
]
gdf = geopandas.GeoDataFrame([1, 2, 3, 4], geometry=points, crs=32630)
gdf.head()

# %%


print(5+5)
