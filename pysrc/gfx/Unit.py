#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Mob import *

class Unit(Mob):
	"""
	A unit is any Mob that belongs to a player. Especially the settlers.
	"""
	
	def __init__(self, viewspace, surface, x, y):
		"""
		"""
		Mob.__init__(self, viewspace, surface, x, y)