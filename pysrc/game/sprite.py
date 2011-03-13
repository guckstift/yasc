
import time

class Sprite :

	"""
	A Sprite is any moveable and animated object in game scene.
	"""
	
	def __init__ (self, display, viewp, surface):
	
		self.display = display
		self.viewp = viewp
		self.surface = surface
		# coordinates
		self.x = 0
		self.y = 0
		# sprite-origin
		self.cx = 0
		self.cy = 0
		# animation settings
		self.animate = False
		self.startframe = 0
		self.endframe = 0
		self.frame = 0
		self.lastframeswitch = None
		self.fps = 20 # frames per second
		self.framelen = 50 # framelength in milliseconds
	
	def ConfigAnimation (self, enable, start, end, first, fps):
	
		self.animate = enable
		if enable:
			self.startframe = start
			self.endframe = end
			self.frame = first
			self.lastframeswitch = None
			self.fps = fps
			self.framelen = 1000.0/fps
	
	def DrawMe (self):
	
		self.surface.DrawToDisplay (self.display, self.x-self.cx, self.y-self.cy, self.frame)

		if self.animate:
			now = time.clock ()
			if self.lastframeswitch == None or (now-self.lastframeswitch)*1000.0 > self.framelen:
				self.lastframeswitch = time.clock()
				self.frame += 1
				if self.frame > self.endframe:
					self.frame = self.startframe


