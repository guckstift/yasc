
import pygame.time

from eventmanager import *
from gamecontroller import *
from gfxengine import *
from viewspace import *
from lowlevellib import *
from gmap import *

class Game :

	"""
	The main game class manages everything, runs the game loop
	"""

	def __init__ (self):
	
		self.lll = LowLevelLib ()
		self.eventmanager = EventManager (self)
		self.gamecontroller = GameController (self)
		self.display = Display ()
		self.viewspace = Viewspace ()
		self.curmap = Map (40)
		# just for test
		self.curmap.heights.setHeight(2,3,-1)
		self.curmap.heights.setHeight(2,5,1)
		self.curmap.heights.setHeight(4,5,-1)
		self.gfxengine = GFXEngine (self.lll, self.display, self.viewspace, self.curmap)
		self.running = False
		self.starttime = 0
				
	def run (self):
	
		self.running = True

		frames = 0
		lasttick = pygame.time.get_ticks ()

		while self.running :
		
			self.eventmanager.tick ()
			self.gamecontroller.tick ()
			self.gfxengine.tick ()
			
			frames += 1
			if pygame.time.get_ticks() - lasttick >= 1000:
				print str(frames)+" fps"+(" - below 40 fps :-( !" if frames<40 else "")
				frames = 0
				lasttick = pygame.time.get_ticks ()

