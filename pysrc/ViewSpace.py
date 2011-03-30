
class ViewSpace:

	"""
	The ViewSpace defines, where the origin of the screen space lays in the gameworld space.
	The gameworld space has its own origin at the upper left corner of the game map.
	The ViewSpace makes scrolling possible through moving its origin.
	"""

	def __init__ (self):
	
		self.origin = (0,0)
