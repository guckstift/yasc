
from sdl.image import *
from OpenGL.GL import *

import surface
from surface import *

class SurfaceSDLOGL (surface.Surface) :
	"""
	Holds both: an sdl-surface and an opengl-2d-texture with the same content
	"""

	def __init__ (self) :
	
		Surface.__init__ (self)
	
	def LoadFromFile (self, filename, bits16=False) :
	
		surface = IMG_Load (filename)
		self.w = surface.w
		self.h = surface.h
		self.byppx = surface.format.BytesPerPixel
		
		if not surface.format.BitsPerPixel == 24:
			raise Exception ("Surface loading of other then 24bit-images not allowed")
		
		if bits16:
			self.byppx = 3
			pixdat16 = []
			for y in range(self.h):
				for x in range(self.w):
					i = y*self.w+x # pixel number
					pixdat16p = (surface.pixels[i*self.byppx+0] * 31 / 255)<<11 # red
					pixdat16p += (surface.pixels[i*self.byppx+1] * 63 / 255)<<5 # green
					pixdat16p += surface.pixels[i*self.byppx+2] * 31 / 255 # blue
					pixdat16.append(pixdat16p)
		
		self.texture = glGenTextures (1)
		glBindTexture (GL_TEXTURE_2D, self.texture)
		glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

		# only if image is RGB,24bit
		if bits16 :
			glTexImage2D (GL_TEXTURE_2D, 0, GL_RGB5,
				self.w, self.h, 0, GL_RGB, GL_UNSIGNED_SHORT_5_6_5, pixdat16)
			#glTexImage2D (GL_TEXTURE_2D, 0, 3,
			#	2, 2, 0, GL_RGB, GL_UNSIGNED_SHORT_5_6_5, [0,0,0,0])
		else:
			glTexImage2D (GL_TEXTURE_2D, 0, 3,
				self.w, self.h, 0, GL_RGB, GL_UNSIGNED_BYTE, surface.pixels.to_array())
				
