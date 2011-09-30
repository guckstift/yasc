#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Mob import *

class Animal(Mob):
	"""
	An animal is a mob that isnt controlled by a player
	"""
	
	def __init__(self, viewspace, surface):
		"""
		"""
		Mob.__init__(self, viewspace, surface)