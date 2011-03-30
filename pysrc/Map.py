
from VertexArray import *
from Terramap import *
from Heightmap import *

class Map :

	"""
	Holds the map data with terrain-info, heigth-map, etc.
	"""

	def __init__ (self, mapsize):
	
		if mapsize<2 or mapsize%2 == 1:
			raise Exception("Mapsize to small (<2) or mapsize is an odd number!")
		
		self.mapsize = mapsize # = kartenbreite = kartenhoehe
		self.terra = Terramap (mapsize)
		self.heights = Heightmap (mapsize)
		self.vertarray = VertexArray (self)
	
	def getVertarray (self):
	
		return self.vertarray
