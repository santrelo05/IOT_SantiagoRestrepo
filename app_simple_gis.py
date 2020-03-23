from shapely.geometry import Point, LineString, Polygon
point1 = Point(6.244889, -75.603854)
point2 = Point(6.241465, -75.590121)
point3 = Point(6.240755, -75.580202)
x = point1.x
y = point1.y
print(x,y)
point_coords = point2.coords
xy = point_coords.xy
print(xy)
point_dist = point1.distance(point2)
print("la distancia es {0:.4f} grados decimales".format(point_dist))
print(point_dist)
# para pasar a km en WGS84 usando la formula de haversine
# https://gis.stackexchange.com/questions/80881/what-is-unit-of-shapely-length-attribute
line1 = LineString([point1,point2,point3])
print("la longitud es {0:.4f}".format(line1.length))
poly1 = Polygon([(2.2,4.2),(7.2,-20.2),(9.45,-6.7)])
centroide = poly1.centroid
area = poly1.area
print("el centroide es ",centroide)
print("el area es {0:.4f}".format(area))

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
fp = "./Data/DAMSELFISH_distributions.shp"
data = gpd.read_file(fp)
type(data)
#data.plot()
#plt.show()

#out = r"./Data/salida1.shp"
#selection = data[0:50]
#selection.to_file(out)

import fiona

newdata = gpd.GeoDataFrame()
newdata['geometry'] = None
coordinates = [(6.244889, -75.603854),(6.044889, -75.803854),(6.344889, -75.803854),(6.244889, -75.703854)]
poly = Polygon(coordinates)
newdata.loc[0,'geometry'] = poly
newdata.loc[0,'Location'] = 'AreaAburra'
print(newdata.crs)

from fiona.crs import from_epsg
#newdata.crs = from_epsg(4326)
#outfile = r'./Data/aburra.shp'
#newdata.to_file(outfile)

import csv
file1 = open('puntosfinca2.csv')
entrada = csv.reader(file1,delimiter=';')
lon = []
lat = []
elev = []
puntos = []
puntos3d = []
for fila in entrada:
   print(fila)
   lat.append(float(fila[1].replace(",",".")))
   lon.append(float(fila[2].replace(",",".")))
   elev.append(float(fila[3].replace(",",".")))
   puntos.append((lon[-1],lat[-1]))
   puntos3d.append((lon[-1],lat[-1],elev[-1]))
poligono = Polygon(puntos)
print("el area del poligono es  ",poligono.area)
datafinca = gpd.GeoDataFrame()
datafinca['geometry'] = None
datafinca.loc[0,'geometry'] = poligono
datafinca.loc[0,'Location'] = 'San Pedro'
datafinca.crs = from_epsg(4326)
outfile = r'./Data/finca.shp'
datafinca.to_file(outfile)
datafinca.plot()
plt.show()
from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(lon,lat,elev,'gray')
plt.show()
