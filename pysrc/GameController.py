import pygame
import gfx.Unit

class GameController :

	"""
	This class should control the whole game events and interactions between the settlers and
	everything. Simply the whole game logic.
	"""

	def __init__ (self, game):
	
		self.game = game
		self.gfxengine = game.getGfxengine()
		self.inputmanager = game.getInputmanager()
		self.last_keyevent = None
		#self.mysettler = Unit(self.gfxengine, 100, 100)
		# create a settler for testing:
		self.unit = self.gfxengine.createSettler(100, 100)
		self.mouse_is_down = False
	
	def tick (self):
	
		"""
		One cycle in the game loop
		"""
		self.moveSettlers()

	def moveSettlers(self):
		"""
		Starts the eventevaluation.
		"""
		self.setSettlerDirectionByKeyevents()
		#self.setSettlerDirectionByMouseevents()
		self.unit.move()


	def setSettlerDirectionByKeyevents(self):
		"""
		Sets the direction and moving variable of the settlers
		"""
		event = self.inputmanager.getLastKeyevent()
		
		if event == None:
			return

		#direction = self.unit.getDirection()
		
		if event.type == pygame.KEYDOWN:  
			self.unit.moving = True
		elif event.type == pygame.KEYUP: 
			self.unit.moving = False
		
		if event.key == 274:
			#direction.set_down(speed)
			pass
		elif event.key == 273:
			#direction.set_up(speed)
			pass
		if event.key == 276:
			self.unit.changeDirection(3)	# towards left
		elif event.key == 275:
			self.unit.changeDirection(0)	# towards right
		
		
			


	"""def setSettlerDirectionByMouseevents(self):
		event = self.inputmanager.getLastMouseevent()
		direction = self.mysettler.getDirection()

		if self.mouse_is_down or event != None and event.type == pygame.MOUSEBUTTONDOWN:  
			self.mouse_is_down = True
			mouse_x,mouse_y = pygame.mouse.get_pos()
			pos_x, pos_y = self.mysettler.getPos()
			direction = self.mysettler.getDirection()

		if mouse_x > pos_x:
			direction.set_right(1) 
			print "right"
		elif mouse_x < pos_x:
			direction.set_left(1) 
			print "left"
		else:
			print "no left right"
			direction.set_left(0) 
			direction.set_right(0) 

		if mouse_y > pos_y:
			print "down!"
			direction.set_down(1)
		elif mouse_y < pos_y:
			print "up"
			direction.set_up(1)
		else:
			print "no up down"
			direction.set_down(0) 
			direction.set_up(0) 

		if event != None and event.type == pygame.MOUSEBUTTONUP:
			self.mouse_is_down = False
			self.mysettler.stop()"""
