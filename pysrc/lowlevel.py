
import ctypes

class LowLevelLib :

	def __init__ (self):
	
		self.view = ctypes.CDLL ("bin/lowlevel/libview.so")

