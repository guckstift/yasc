
from sdl import *
from OpenGL.GL import *

import display
from display import *

class DisplaySDLOGL (display.Display) :

	"""
	Represents the SDL+OpenGL based Display
	"""

	def __init__ (self, resol=(800,600), wincaption="SDL Display"):
	
		Display.__init__ (self)

		self.resol = resol
		self.midp = (resol[0]/2, resol[1]/2)
		self.bitdepth = 32

		SDL_Init (SDL_INIT_VIDEO)
		
		SDL_WM_SetCaption (wincaption, wincaption)
		
		if self.bitdepth == 32:
			SDL_GL_SetAttribute (SDL_GL_RED_SIZE, 8)
			SDL_GL_SetAttribute (SDL_GL_GREEN_SIZE, 8)
			SDL_GL_SetAttribute (SDL_GL_BLUE_SIZE, 8)
			SDL_GL_SetAttribute (SDL_GL_ALPHA_SIZE, 8)
			SDL_GL_SetAttribute (SDL_GL_BUFFER_SIZE, 32)
		else:
			raise Exception ("Other bitdepths than 32 bits currently not supportet by DisplaySDLOGL") 

		SDL_GL_SetAttribute (SDL_GL_DOUBLEBUFFER, 1)
		SDL_GL_SetAttribute (SDL_GL_DEPTH_SIZE, 0)
		SDL_GL_SetAttribute (SDL_GL_STENCIL_SIZE, 0)
		SDL_GL_SetAttribute (SDL_GL_ACCUM_RED_SIZE, 0)
		SDL_GL_SetAttribute (SDL_GL_ACCUM_GREEN_SIZE, 0)
		SDL_GL_SetAttribute (SDL_GL_ACCUM_BLUE_SIZE, 0)
		SDL_GL_SetAttribute (SDL_GL_ACCUM_ALPHA_SIZE, 0)
		SDL_GL_SetAttribute (SDL_GL_STEREO, 0)
		SDL_GL_SetAttribute (SDL_GL_MULTISAMPLEBUFFERS, 0)
		SDL_GL_SetAttribute (SDL_GL_MULTISAMPLESAMPLES, 0)
		SDL_GL_SetAttribute (SDL_GL_SWAP_CONTROL, 0)
		SDL_GL_SetAttribute (SDL_GL_ACCELERATED_VISUAL, 0)

		self.screen = SDL_SetVideoMode (resol[0], resol[1], self.bitdepth, SDL_OPENGL)
		
		glEnable (GL_TEXTURE_2D)
		
		glClearColor (0,0,0,1)
		
		glMatrixMode (GL_PROJECTION)
		glLoadIdentity ()
		glOrtho (0.0, float(resol[0]), float(resol[1]), 0.0, -1.0, 1.0)
	
	def ShowFrame (self):
	
		SDL_GL_SwapBuffers ()

	def Clear (self):
	
		glClear (GL_COLOR_BUFFER_BIT)
