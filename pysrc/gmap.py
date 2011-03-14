
import ctypes

from vertexarray import *

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
		self.vertarray = Vertexarray (self)
	
	def getVertarray (self):
	
		return self.vertarray

class Terramap :

	"""
	This class holds an array of terrain-types for each triangle.
	"""

	def __init__ (self, mapsize):
	
		self.mapsize = mapsize
		self.data = [[0 for x in range(mapsize)] for y in range(mapsize)]
		self.carr = None

	def asCArray (self):

		if self.carr == None:

			UINT = ctypes.c_uint
			PUINT = ctypes.POINTER(UINT)
			PPUINT = ctypes.POINTER(PUINT)
			UINTARR = UINT * self.mapsize
			PUINTARR = PUINT * self.mapsize
			self.carr = PUINTARR ()
			for y in range(self.mapsize):
				self.carr[y] = UINTARR ()
				for x in range(self.mapsize):
					self.carr[y][x] = self.data[y][x]
		
		return self.carr
	
	def setTria (self, x, y, terra) :
	
		self.data[y][x] = terra
		if not self.carr == None:
			self.carr[y][x] = terra

class Heightmap :

	"""
	This class holds an array of height-values (integer) for each vertex.
	"""

	def __init__ (self, mapsize):
	
		self.vwi = 1+(mapsize/2) # vertices per line
		self.vhe = 1+mapsize # vertex-line-count
		self.data = [[0 for x in range(self.vwi)] for y in range(self.vhe)] # hights of vertices
		self.carr = None

	def asCArray (self):

		if self.carr == None:

			INT = ctypes.c_int
			PINT = ctypes.POINTER(INT)
			INTARR = INT * self.vhe
			PINTARR = PINT * self.vwi
			self.carr = PINTARR ()
			for y in range(self.vhe):
				self.carr[y] = INTARR ()
				for x in range(self.vwi):
					self.carr[y][x] = self.data[y][x]
		
		return self.carr
	
	def setHeight (self, x, y, height) :
	
		self.data[y][x] = height
		if not self.carr == None:
			self.carr[y][x] = height


