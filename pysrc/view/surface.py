
class Surface :

	"""
	A generic surface class. Subclasses of this class implement a class which holds a 2-dimensional
	graphic for a certain technology (eg. OpenGL-Texture).
	Instanciating this class gives an empty graphic with dimensions of (0,0).
	"""

	def __init__ (self) :
	
		# dimensions
		self.w = self.h = 0
		# framing
		self.cols = self.rows = 1
	
	def LoadFromFile (self, filename) :
	
		"""
		Does nothing. Subclasses should implement this method to load an image from the file
		"filename".
		"""
	
		pass
	
	def DrawToDisplay (self, display, x, y, frame=0) :
	
		"""
		Does nothing. Subclasses should implement this method to draw a specific frame of or the
		whole surface to a Display on the position x,y with its top-left corner.
		"""
	
		pass
