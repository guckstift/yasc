
import pygame

class EventManager :

	"""
	This class processes incoming user events
	"""

	def __init__ (self, game):
	
		self.game = game
		
		pygame.init ()
	
	def tick (self):
	
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				self.game.running = False
			elif event.type == pygame.QUIT:
				self.game.running = False

