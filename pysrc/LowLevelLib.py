
import ctypes
import platform
import math
import sys
import string

class LowLevelLib :

	"""
	Provides access to project-own c-libraries
	"""

	def __init__ (self):

		# create platform-specific token (like "linux64", "windows32")
		intbitlen = int(round(math.log(sys.maxint,2))+1)
		pfid = str.lower(platform.system()) + str(intbitlen)

		# load the libraries from the according directory
		self.view = ctypes.CDLL ("bin/"+pfid+"/lowlevel/libview.so")

