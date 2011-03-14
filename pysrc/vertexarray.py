
import ctypes

from constants import *

class Vertexarray :

	"""
	This class supplies an array of 2D-vertices of a given map (currently only as 3D-c-types-array)
	Next thing will be an OpenGL-vertexbuffer or something.
	"""
	
	def __init__ (self, mymap):
	
		self.mymap = mymap
		self.carr = None
	
	def asCArray (self):

		if self.carr == None:

			INT = ctypes.c_int
			PINT = ctypes.POINTER(INT)
			PPINT = ctypes.POINTER(PINT)
			POINT = INT * 2
			VERTLINE = PINT * self.mymap.heights.vwi
			VERTMAP = PPINT * self.mymap.heights.vhe
			self.carr = VERTMAP ()
			for y in range(self.mymap.heights.vhe):
				self.carr[y] = VERTLINE ()
				for x in range(self.mymap.heights.vwi):
					self.carr[y][x] = POINT ()
					self.carr[y][x][0], self.carr[y][x][1] = (
						x*TRIA_W + TRIA_W/2*(y%2), y*TRIA_H - self.mymap.heights.data[y][x]*HEIGHT_UNIT_PX)
		
		return self.carr

