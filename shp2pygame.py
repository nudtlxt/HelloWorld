# Connection funcitons between Shapefile and pygame.
import os
import geopandas as gp
from geopy.distance import vincenty

shp = gp.GeoDataFrame.from_file('shapefiles/ctd_data.shp')

corrd1 = (shp.geometry.total_bounds[1],shp.geometry.total_bounds[2])
corrd2 = (shp.geometry.total_bounds[3],shp.geometry.total_bounds[2])
corrd3 = (shp.geometry.total_bounds[1],shp.geometry.total_bounds[0])
corrd4 = (shp.geometry.total_bounds[3],shp.geometry.total_bounds[0])

y_range = vincenty(corrd1,corrd2).m + 100
x_range = vincenty(corrd1,corrd3).m + 100

