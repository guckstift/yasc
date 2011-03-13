
from sdl import *
from sdl.image import *
from OpenGL.GL import *

import surface
from surface import *

class SurfaceSDLOGL (surface.Surface) :

	"""
	Holds a 2D-graphic as an OpenGl-Texture. Loading from file uses an SDL-function.
	"""

	def __init__ (self) :
	
		Surface.__init__ (self)
	
	def LoadFromFile (self, filename, bits16=False) :
	
		"""
		Load image from png file. Currently png files must be 24bit or 32bit-images.
		@param bits16: True if texture should be 16bit in memory (R5G6B5)
		"""
		
		self.texture = glGenTextures (1)
		glBindTexture (GL_TEXTURE_2D, self.texture)
		glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	
		surface = IMG_Load (filename)
		self.w = surface.w
		self.h = surface.h
		self.byppx = surface.format.BytesPerPixel
		
		if self.byppx == 3:
		
			if bits16:
				fixedsurf = SDL_CreateRGBSurface (SDL_SWSURFACE, self.w, self.h, 16,
					0xf800, 0x7e0, 0x1f, 0)
				SDL_BlitSurface (surface, None, fixedsurf, None)

			if bits16 :
				glTexImage2D (GL_TEXTURE_2D, 0, GL_RGB5,
					self.w, self.h, 0, GL_RGB, GL_UNSIGNED_SHORT_5_6_5, fixedsurf.pixels.to_array())
			else:
				glTexImage2D (GL_TEXTURE_2D, 0, 3,
					self.w, self.h, 0, GL_RGB, GL_UNSIGNED_BYTE, surface.pixels.to_array())
					
		elif self.byppx == 4:
		
			if bits16:
				fixedsurf = SDL_CreateRGBSurface (SDL_SWSURFACE, self.w, self.h, 16,
					0xf800, 0x7e0, 0x1f, 0)
				SDL_BlitSurface (surface, None, fixedsurf, None)
			else:
				fixedsurf = SDL_CreateRGBSurface (SDL_SWSURFACE, self.w, self.h, 32,
					0xff000000, 0xff0000, 0xff00, 0xff)
				SDL_SetAlpha(surface, 0,0)
				SDL_BlitSurface (surface, None, fixedsurf, None)

			if bits16 :
				glTexImage2D (GL_TEXTURE_2D, 0, GL_RGB5,
					self.w, self.h, 0, GL_RGB, GL_UNSIGNED_SHORT_5_6_5, fixedsurf.pixels.to_array())
			else:
				glTexImage2D (GL_TEXTURE_2D, 0, 4,
					self.w, self.h, 0, GL_RGBA, GL_UNSIGNED_INT_8_8_8_8, fixedsurf.pixels.to_array())
		
		else:
		
			raise Exception ("Surface loading of other then 24bit or 32bit-images not allowed")
	
	def DrawToDisplay (self, display, x, y, frame=0) :
	
		glEnable (GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glBindTexture (GL_TEXTURE_2D, self.texture)
		glBegin (GL_QUADS)
		
		row = frame / self.cols
		col = frame % self.cols
		
		glTexCoord2f (float(col)/self.cols, float(row)/self.rows)
		glVertex3i (x+0, y+0, 0)
		
		glTexCoord2f (float(col)/self.cols, float(row+1)/self.rows)
		glVertex3i (x+0, y+self.h/self.rows, 0)
		
		glTexCoord2f (float(col+1)/self.cols, float(row+1)/self.rows)
		glVertex3i (x+self.w/self.cols, y+self.h/self.rows, 0)
		
		glTexCoord2f (float(col+1)/self.cols, float(row)/self.rows)
		glVertex3i (x+self.w/self.cols, y+0, 0)
		
		glEnd ()
		
		
		

