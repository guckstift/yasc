
class Display :

	"""
	A generic Display to output the game scene.
	It's useless without any subclass.
	"""

	def __init__ (self):
	
		self.screen = None
		self.resol = (0,0) # screen-resolution
		self.midp = (0,0) # screen-midpoint
	
	def ShowFrame (self):
	
		pass
	
	def Clear (self):
	
		pass
