
import pygame

class Sprite :

	"""
	A Sprite is any moveable or immobile, animated object in game scene.
	"""
	
	def __init__ (self, viewspace, surface):
	
		self.viewspace = viewspace
		self.surface = surface
		# coordinates (screen-coordinates)
		self.x = 0
		self.y = 0
		# sprite-origin
		self.cx = 0
		self.cy = 0
		# animation settings
		self.animate = False
		self.startframe = 0
		self.endframe = 0
		self.frame = 0.0
		self.startframetime = 0
		self.fps = 20 # frames per second
		self.framelen = 50 # framelength in milliseconds
	
	def configAnimation (self, enable, start, end, fps):
	
		self.animate = enable
		if enable:
			self.startframe = start
			self.endframe = end
			self.frame = start
			self.startframetime = 0
			self.fps = fps
			self.framelen = 1000.0/fps
	
	def drawToDisplay (self, display):
	
		# this snippet ensures a time-precise correct floating animation 
		if self.animate:
			now = pygame.time.get_ticks()
			if self.startframetime == 0:
				self.startframetime = now
			timedistance = now-self.startframetime
			framedistance = float(timedistance)/float(self.framelen)
			self.frame = self.startframe + framedistance
			if int(self.frame) > self.endframe:
				self.frame = self.startframe
				self.startframetime = self.startframetime + self.framelen*(1+self.endframe-self.startframe)

		self.surface.drawToDisplay (display, self.x-self.cx, self.y-self.cy, int(self.frame))

