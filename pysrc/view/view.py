
class View :

	"""
	Represents the scrolling-coordinates, these are pixel-coordinates where the screen-midpoint lays
	in the map-space.
	"""

	def __init__ (self, viewp=(0,0)):
	
		self.vpt = viewp # the screen-midpoint on the map in pixels
