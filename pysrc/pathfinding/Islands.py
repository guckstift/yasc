#!/usr/bin/env python
#-*- coding:utf-8 -*-

import Pathfinder

class Islands:
	"""
	This class manages the so called "islands", areas not reachable one below the other.
	Its important for the pathfinding algorithm, otherwise he will look at the hole island
	for the endpoint.
	# TODO: sending of obstacle map between Islands and Pathfinder (successorscalculation)
	"""
	def __init__(self):
		"""
		Initializes the dictionary with coordinates as keys and a positiv number for
		every island as value.
		"""
		self.islands = {}
		
	def getIslands(self, islands):
		"""
		If there is a correct dictionary you can input it here.
		@param islands the dictionary with coordinates as keys and islands as values
		"""
		self.islands = islands

	def searchIslands(self, obstacle_map):
		"""
		Iterates over the nodes of the obstaclemap and tags every island with an 
		distinct positiv number.
		@param obstacle_map array of rows, True for blocked node
		"""
		tag = 0	# every island gets a unique tag
		
		for y in range(len(obstacle_map)):
			for x in range(len(obstacle_map[0])):	# y instead of 0 should work too
				# if node in obstacle_map is not blocked and node is not in already visited:
				if (not obstacle_map[x][y]) and ((x,y) not in self.islands.keys()):
					self._fill((x,y), tag)
					tag = tag + 1
		
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

	def _fill(self, start_coord, island_tag):
		"""
		Usesd by the searchIslands method. Gets a hole area (island) by using the iterative floodfilling algorithm.
		@param start_coord the coordinate to start with the floodfill algorithm
		@param island_tag the tag for this specific island
		"""
		stack = []
		
		stack.append(coord_start)

		while stack != []:
			coord = stack.pop(0)

			if (coord not in self.islands.keys()):
				self.islands[coord] = island_tag

			successors = Pathfinder.successors(coord)
			
			for entry in successors:
				stack.append(entry)
