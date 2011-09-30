
import pygame

class InputManager :

	"""
	This class processes incoming user events
	"""

	def __init__ (self, game):
	
		self.game = game
		self.key_queue = []
		self.mouse_queue = []
		
		pygame.init ()
	
	def process (self):
	
		"""
		Process all new events
		"""
	
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
				#self.game.running = False
				self.key_queue.append(event)
			elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
				self.mouse_queue.append(event)
			elif event.type == pygame.QUIT:
				self.game.running = False
	
	def getLastKeyevent(self):  
		"""
		@return: the oldest key event in the event queue or None if list is empty
		"""
		if len(self.key_queue) == 0:
			ret = None
		else:  
			ret = self.key_queue.pop(0)
			return ret

	def getLastMouseevent(self):  
		"""
		@return: the oldest key event in the event queue or None if list is empty
		"""
		if len(self.mouse_queue) == 0:
			ret = None
		else:  
			ret = self.mouse_queue.pop(0)
			return ret

