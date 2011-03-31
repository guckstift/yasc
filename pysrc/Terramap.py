
import ctypes

class Terramap :

	"""
	This class holds an array of terrain-types for each triangle.
	"""

	def __init__ (self, mapsize):
	
		self.mapsize = mapsize
		self.data = [[0 for x in range(mapsize)] for y in range(mapsize)]
		self.carr = None

	def asCArray (self):
	
		"""
		Height-map as 2-dimensional C unsigned-int-array (unsigned int**) (lines*cols*uint)
		"""

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
