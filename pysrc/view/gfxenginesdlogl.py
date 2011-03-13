
import ctypes as ct
from sdl import *

import gfxengine
from gfxengine import *
from surfacesdlogl import *

class GFXEngineSDLOGL (gfxengine.GFXEngine) :

	"""
	The SDL+OpenGL-based GFX-Engine of yasc
	"""

	def __init__ (self, ll, display=None, view=None, mymap=None) :
	
		GFXEngine.__init__ (self, display, view, mymap)
		self.ll = ll
	
	def LoadTerrainset (self) :
	
		self.terrainset = Terrainset ()
		
	def DrawTerrain (self) :
	
		self.ll.view.GFXEngineSDLOGL_DrawTerrain (self.mymap.terra.asCArray (),
			self.mymap.mapsize, TRIA_W, TRIA_H,
			TEX_FACTOR, self.terrainset.asCArray(), self.vertarr.asCArray())
		
		"""
		#
		# This code was reimplemented in the C-function GFXEngineSDLOGL_DrawTerrain () in view.c
		# performance-improvement 14ms -> 3ms
		#
		"""

class Terrainset :

	"""
	This class holds all terrain-graphics and darker and lighter versions of each
	"""

	def __init__ (self):
	
		self.tcount = len(TERRAIN_TEXTURE_FILES)
		self.data = []
		for terrafilename in TERRAIN_TEXTURE_FILES :
			newsurf = SurfaceSDLOGL ()
			newsurf.LoadFromFile (TERRAIN_PNG_DIR +"/"+ terrafilename, True)
			self.data.append (newsurf)
		self.carr = None

	def asCArray (self):

		if self.carr == None:

			UINT = ct.c_uint
			UINTARR = UINT * self.tcount
			self.carr = UINTARR ()
			for i in range(self.tcount):
				self.carr[i] = self.data[i].texture
		
		return self.carr

