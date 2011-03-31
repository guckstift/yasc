
import ctypes

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
	
		"""
		Height-map as 2-dimensional C int-array (int**)
		"""

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
	
		"""
		Set a single Height-value at (x,y) to height
		"""
	
		self.data[y][x] = height
		if not self.carr == None:
			self.carr[y][x] = height

