
class Surface :

	"""
	A generic surface class. Subclasses of this class implement a class which holds a 2-dimensional
	graphic for a certain technology (eg. OpenGL-Texture).
	Instanciating this class gives an empty graphic with dimensions of (0,0).
	"""

	def __init__ (self) :
	
		self.w = self.h = 0
	
	def LoadFromFile (self, filename) :
	
		"""
		Does nothing. Subclasses should implement this method to load an image from the file
		"filename".
		"""
	
		pass
