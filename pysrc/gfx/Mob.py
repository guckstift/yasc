#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Sprite import *

class Mob(Sprite):
	"""
	A mob is any moveable, animated object in the game.
	"""
	
	def __init__(self, viewspace, surface, x, y):
		"""
		Sets the moving variable to False - so mob isnt moving.
		Sets the speed of the mob to 1.
		"""
		Sprite.__init__(self, viewspace, surface, x, y)
		#print sprite.printfps()
		self.moving = False
		self.speed = 1
		
	def move(self):
		"""
		Let the mob move if moving is True and start the animation.
		If moving is False the animation will be stopped.
		"""
		if self.moving == True:
			if self.direction == 0:
				self.x += self.speed
			elif self.direction == 1:
				pass
			elif self.direction == 2:
				pass
			elif self.direction == 3:
				self.x -= self.speed
			elif self.direction == 4:
				pass
			elif self.direction == 5:
				pass
			
			self.startAnimation()
		else:
			self.stopAnimation()
		
		"""self.y += self.direction.down
		self.y -= self.direction.up
		self.x -= self.direction.left
		self.x += self.direction.right"""
		

	def changeDirection(self, direction):
		"""
		@param direction: a number representing one of the 6 possible directions
		"""
		self.direction = direction