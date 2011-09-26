#!/usr/bin/env python
#-*- coding:utf-8 -*-

class BuildingRecipes:
	"""
	"""
	
	def __init__(self):
		"""
		"""
		self.building_recipes = {}

		self.building_recipes["lumberjackshome"] = lumberjackshouse = {}
		self.building_recipes["sawmill"] = sawmill = {}
		self.building_recipes["masonshouse"] = masonshouse = {}
		self.building_recipes["forestershouse"] = forestershouse = {}


		lumberjackshouse["plank"] = 3

		sawmill["plank"] = 3
		sawmill["stone"] = 1

		masonshouse["plank"] = 2
		masonshouse["stone"] = 2

		forestershouse["plank"] = 2


