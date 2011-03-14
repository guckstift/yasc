
import pygame
from OpenGL.GL import *

class Surface :

	"""
	A Surface holds an 2d-image ready to be drawn to a Display
	"""

	def __init__ (self) :
	
		# dimensions
		self.w = self.h = 0
		# framing
		self.cols = self.rows = 1
	
	def loadFromFile (self, filename, bits16=False) :
	
		"""
		Load image from png file. Currently png files must be 24bit or 32bit-images.
		@param bits16: True if texture should be 16bit in memory (R5G6B5)
		"""
		
		self.texture = glGenTextures (1)
		glBindTexture (GL_TEXTURE_2D, self.texture)
		glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	
		surface = pygame.image.load (filename)
		self.w, self.h = surface.get_size()
		self.byppx = surface.get_bytesize()
		
		if self.byppx == 3:
		
			print "24bit"
		
			if bits16:
				print "->16bit"
				fixedsurf = pygame.Surface ((self.w, self.h), 0, 16, (0xf800, 0x7e0, 0x1f, 0))
				fixedsurf.blit (surface, surface.get_rect())
				glTexImage2D (GL_TEXTURE_2D, 0, GL_RGB5,
					self.w, self.h, 0, GL_RGB, GL_UNSIGNED_BYTE, pygame.image.tostring (fixedsurf,"RGB"))
			else:
				print "nochange"
				glTexImage2D (GL_TEXTURE_2D, 0, 3,
					self.w, self.h, 0, GL_RGB, GL_UNSIGNED_BYTE, pygame.image.tostring (surface,"RGB"))
					
		elif self.byppx == 4:
		
			print "32bit"
		
			if bits16:
				print "->16bit"
				fixedsurf = pygame.Surface ((self.w, self.h), 0, 16, (0xf800, 0x7e0, 0x1f, 0))
				fixedsurf.blit (surface, surface.get_rect())
				glTexImage2D (GL_TEXTURE_2D, 0, GL_RGB5,
					self.w, self.h, 0, GL_RGB, GL_UNSIGNED_BYTE, pygame.image.tostring (fixedsurf,"RGB"))
			else:
				glTexImage2D (GL_TEXTURE_2D, 0, 4,
					self.w, self.h, 0, GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring (surface,"RGBA"))
		
		else:
		
			raise Exception ("Surface loading of other then 24bit or 32bit-images not allowed")
	
	def drawToDisplay (self, display, x, y, frame=0) :
	
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
