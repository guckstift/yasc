#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Islands:
	"""
	This class manages the so called "islands", areas not reachable one below the other.
	Its important for the pathfinding algorithm, otherwise he will look at the hole island
	for the endpoint.
	"""
	def __init__(self):
		"""
		Initializes the dictionary with coordinates as keys and a positiv number for
		every island as value.
		"""
		self.islands = {}
		
	def getIslands(self, islands)
		"""
		If there is a correct dictionary you can input it here.
		@param islands the dictionary with coordinates as keys and islands as values
		"""
		self.islands = islands

	def searchIslands(self, obstacle_map):
		"""
		Iterates over the nodes of the obstaclemap and tags every island with an 
		distinct positiv number.
		@param obstacle_map
		"""
		pass
		
	def sameIsland(self, start, end):
		"""
		Gets two tuples and returns True whether the two points are at the same island.
		@param start the startpoint of the pathfindingalgorithm
		@param end the endpoint of the pathfindingalgorithm
		@return True if the two points are at the same island, False otherwise
		"""
		if self.islands[start] == self.islands[end]:
			return True

		return False
