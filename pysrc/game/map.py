
import ctypes as ct

class Map :

	"""
	Holds the map data with terrain-info, heigth-map, etc.
	"""

	def __init__ (self, mapsize):
	
		if mapsize<2 or mapsize%2 == 1:
			raise Exception("Mapsize to small (<2) or mapsize is an odd number!")
		
		self.mapsize = mapsize # = kartenbreite = kartenhoehe
		self.terra = Terramap (mapsize)
		self.hights = Heightmap (mapsize)

class Terramap :

	def __init__ (self, mapsize):
	
		self.mapsize = mapsize
		self.data = [[0 for x in range(mapsize)] for y in range(mapsize)]
		self.carr = None

	def asCArray (self):

		if self.carr == None:

			UINT = ct.c_uint
			PUINT = ct.POINTER(UINT)
			PPUINT = ct.POINTER(PUINT)
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

	def __init__ (self, mapsize):
	
		self.mapsize = mapsize
		self.vwi = 1+(mapsize/2) # vertices per line
		self.vhe = 1+mapsize # vertex-line-count
		self.data = [[0 for x in range(self.vwi)] for y in range(self.vhe)] # hights of vertices
		self.carr = None

	def asCArray (self):

		if self.carr == None:

			INT = ct.c_int
			PINT = ct.POINTER(INT)
			PPINT = ct.POINTER(PINT)
			INTARR = INT * self.vhe
			PINTARR = PINT * self.vwi
			self.carr = PINTARR ()
			for y in range(self.vhe):
				self.carr[y] = INTARR ()
				for x in range(self.vwi):
					self.carr[y][x] = self.data[y][x]
		
		return self.carr
	
	def setHight (self, x, y, hight) :
	
		self.data[y][x] = hight
		if not self.carr == None:
			self.carr[y][x] = hight


