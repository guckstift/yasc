
import ctypes
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
		"""
		This loads all terrain-graphics and creates darker and lighter versions of each
		"""
	
		self.terrainset = []
		
		for terrafilename in TERRAIN_TEXTURE_FILES :
			newsurf = SurfaceSDLOGL ()
			newsurf.LoadFromFile (TERRAIN_PNG_DIR +"/"+ terrafilename, True)
			self.terrainset.append (newsurf)
	
		
	def DrawTerrain (self) :
	
		self.ll.view.GFXEngineSDLOGL_DrawTerrain (self.mymap.terrAsCarray (),
			self.mymap.mapsize, TRIA_W, TRIA_H,
			TEX_FACTOR, self.terrainsetTexturesAsCarray ())
		
		"""
		#
		# This code was reimplemented in the C-function GFXEngineSDLOGL_DrawTerrain () in view.c
		# performance-improvement 14ms -> 3ms
		#
		# original code in superclass
		#
		"""
	
	def DrawTriangle (self, x, y, upt=False) :
	
		
		self.ll.view.GFXEngineSDLOGL_DrawTriangle (x, y, int(upt), TRIA_W, TRIA_H, TEX_FACTOR,
			 self.terrainset[0].texture)
		
		"""
		#
		# This code was reimplemented in the C-function GFXEngineSDLOGL_DrawTriangle () in view.c
		# performance-improvement 50ms -> 14ms
		#
		# original code:
		
		tx = x
		ty = y
		x = tx*TRIA_W/2
		y = ty*TRIA_H

		u = (tx/(TEX_FACTOR*2.0)) + 0.5 * int( (ty%(TEX_FACTOR*2)) >= TEX_FACTOR )
		v = (ty/float(TEX_FACTOR))

		glBindTexture (GL_TEXTURE_2D, self.terrainset[0].texture)
		glBegin (GL_TRIANGLES)
		if not upt:
			glTexCoord2f (u, v)
			glVertex3i (x, y, 0)
		
			glTexCoord2f (u+(1.0/TEX_FACTOR), v)
			glVertex3i (x+TRIA_W, y, 0)
		
			glTexCoord2f (u+(1.0/(TEX_FACTOR*2)), v+(1.0/TEX_FACTOR))
			glVertex3i (x+TRIA_W/2, y+TRIA_H, 0)
		
		else :
			glTexCoord2f (u+(1.0/(TEX_FACTOR*2)), v)
			glVertex3i (x+TRIA_W/2, y, 0)
		
			glTexCoord2f (u+(1.0/TEX_FACTOR), v+(1.0/TEX_FACTOR))
			glVertex3i (x+TRIA_W, y+TRIA_H, 0)
			
			glTexCoord2f (u, v+(1.0/TEX_FACTOR))
			glVertex3i (x, y+TRIA_H, 0)
		
		glEnd ()
		"""
	
	def terrainsetTexturesAsCarray (self) :
		"""
		Returns the opengl-texture-names of the terrain-textures
		as a ctype-uint-array
		"""
		
		intarr = ctypes.c_uint * len(self.terrainset)
		
		res = intarr()
		for i in range(len(self.terrainset)) :
			res[i] = self.terrainset[i].texture

		return res

