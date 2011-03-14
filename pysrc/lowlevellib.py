
import ctypes

class LowLevelLib :

	"""
	Provides access to project-own c-libraries
	"""

	def __init__ (self):
	
		self.view = ctypes.CDLL ("bin/lowlevel/libview.so")

