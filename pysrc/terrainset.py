
import ctypes

from surface import *
from constants import *

class Terrainset :

	"""
	This class holds all terrain-graphics and darker and brighter versions of each
	"""

	def __init__ (self):
	
		self.tcount = len(TERRAIN_TEXTURE_FILES)
		self.data = []
		for terrafilename in TERRAIN_TEXTURE_FILES :
			newsurf = Surface ()
			newsurf.loadFromFile (TERRAIN_PNG_DIR +"/"+ terrafilename, True)
			self.data.append (newsurf)
		self.carr = None

	def asCArray (self):

		if self.carr == None:

			UINT = ctypes.c_uint
			UINTARR = UINT * self.tcount
			self.carr = UINTARR ()
			for i in range(self.tcount):
				self.carr[i] = self.data[i].texture
		
		return self.carr

