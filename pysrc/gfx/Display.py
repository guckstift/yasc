
import pygame
from OpenGL.GL import *

class Display:

	"""
	Represents the Output-Window or Screen
	"""
	
	def __init__ (self):
	
		self.resolution = (800,600) # screen-resolution
		self.bitdepth = 24
		
		pygame.display.init ()
		
		pygame.display.set_caption ("PyGame Window")
		
		if self.bitdepth == 24:
			pygame.display.gl_set_attribute (pygame.GL_ALPHA_SIZE, 0)
			pygame.display.gl_set_attribute (pygame.GL_RED_SIZE, 8)
			pygame.display.gl_set_attribute (pygame.GL_GREEN_SIZE, 8)
			pygame.display.gl_set_attribute (pygame.GL_BLUE_SIZE, 8)
			pygame.display.gl_set_attribute (pygame.GL_BUFFER_SIZE, 24)
		else:
			raise Exception ("Other bitdepths than 24 bits currently not supportet by Display") 

		pygame.display.gl_set_attribute (pygame.GL_DOUBLEBUFFER, 1)
		pygame.display.gl_set_attribute (pygame.GL_DEPTH_SIZE, 0)
		pygame.display.gl_set_attribute (pygame.GL_STENCIL_SIZE, 0)
		pygame.display.gl_set_attribute (pygame.GL_ACCUM_RED_SIZE, 0)
		pygame.display.gl_set_attribute (pygame.GL_ACCUM_GREEN_SIZE, 0)
		pygame.display.gl_set_attribute (pygame.GL_ACCUM_BLUE_SIZE, 0)
		pygame.display.gl_set_attribute (pygame.GL_ACCUM_ALPHA_SIZE, 0)
		pygame.display.gl_set_attribute (pygame.GL_STEREO, 0)
		pygame.display.gl_set_attribute (pygame.GL_MULTISAMPLEBUFFERS, 0)
		pygame.display.gl_set_attribute (pygame.GL_MULTISAMPLESAMPLES, 0)
		pygame.display.gl_set_attribute (pygame.GL_SWAP_CONTROL, 0)
		pygame.display.gl_set_attribute (pygame.GL_ACCELERATED_VISUAL, 0)

		pygame.display.set_mode (self.resolution, pygame.OPENGL|pygame.DOUBLEBUF, self.bitdepth)
		
		glEnable (GL_TEXTURE_2D)
		
		glClearColor (0,0,0,1)
		
		glMatrixMode (GL_PROJECTION)
		glLoadIdentity ()
		glOrtho (0.0, float(self.resolution[0]), float(self.resolution[1]), 0.0, -1.0, 1.0)
	
	def clear (self):
	
		"""
		Clear what is currently in the Framebuffer
		"""
	
		glClear (GL_COLOR_BUFFER_BIT)
	
	def showFrame (self):
	
		"""
		Make the current drawings visible
		"""
	
		pygame.display.flip ()
