#!/usr/bin/env python
#-*- coding:utf-8 -*-

from path_heuristic import *
from priorityqueueset import PriorityQueueSet
from pathstorage import *

class Pathfinder (object):
	"""
	The class organizing everything about pathfinding.
	Needs following files:
		path_heuristic.py
		priorityqueueset.py
		pathstorage.py
		
	TODO: 	*no error if coord is greater than border
		*sometimes not the direct path is chosen, if another one has the 
		same length
		*not storing reversed pathes
		*speed-tweaks by resizing the triangles (x4, x16 ...)
		*how to recognize not reachable areas?
	"""

	def __init__(self):
		self.pathstorage = Pathstorage()

	class Node (object):
		"""
		Represents a single node at the map
		"""

		def __init__(self, coord, g = None, pred = None):
			"""
			@param coord the coordinates of the node
			@param g the cost from the startpoint to this point
			@param pred a reference to the predecessor
			"""
			self.coord = coord	# the coordinates of this point
			self.gcost = g		# the cost from the startpoint to this point
			self.hcost = None	# the heuristic cost from this point to the endpoint
			self.pred = pred	# the predecessor of this point at the path
	
		def __eq__(self, other):
			return self.coord == other.coord
		
		def __cmp__(self, other):
			return cmp(self.get_fcost(), other.get_fcost())
		
		def __hash__(self):
			return hash(self.coord)
				
		def get_fcost(self):
			"""
			Returns the cost f(x) of this node
			"""
			return self.gcost + self.hcost
		

	def compute_path(self, start, end):
		"""
		Implements the A-Star algorithm (computes the path between start- and endpoint)
		The path is returned as an iterator to the points, 
		including the start- and endpoints themselves.
		@param start a 2-tuple with x- and y-coordinate of the startpoint
		@param end same as start
		@return if a path could be found it will be returned. If no path was found, 
		an empty list is returned.
		"""
		# if the start- and endpoints are stored already, the stored path will be
		# returned:
		path = self.pathstorage.search_path((start, end))
		if path != []:
			return path
		
		# if the path isn't stored, it will be calculated:
		sx = start[0]
		sy = start[1]
		ex = end[0]
		ey = end[1]
		closed_set = {}	# the set with the nodes along the path
		open_set = PriorityQueueSet()	# nodes which are possible for the path
		start_node = self.Node((sx, sy), 0, None)
		start_node.hcost = path_heuristic((sx, sy), (ex, ey))
		open_set.add(start_node)
	
		while len(open_set) > 0:
			curr_node = open_set.pop_smallest()
		    
			if curr_node.coord == (ex, ey):
				path = self._reconstruct_path(curr_node)
				# make a list from the iterator "path" (more handy):
				nodelist = []
				for entry in path:
					nodelist.append(entry)
					
				self.pathstorage.add(nodelist)
				return nodelist
		
			closed_set[curr_node] = curr_node
		
			for succ_coord in self._successors(curr_node.coord):
				succ_node = self.Node(succ_coord)
				succ_node.gcost = curr_node.gcost + 1	# the cost from one node to another is always 1
				succ_node.hcost = path_heuristic(succ_node.coord, (ex, ey))
			
				if succ_node in closed_set:
					continue
				
				if open_set.add(succ_node):
					succ_node.pred = curr_node
				
		return []

	def _successors(self, coord, border=6):
		"""
		Computes all possible successors of the given coord
		@param coord the coordinate whoms successors will be computed
		@param border x- and y-coordinate of the right and lower border
		@return a List with all successing nodes
		"""
		succ_list = []	# list with all possible successors of the given node
	
		if (coord[0] > 0 and coord[1] > 0) and (coord[0] < border and coord[1] < border):
			succ_list.append((coord[0]-1, coord[1]))
			succ_list.append((coord[0], coord[1]-1))
			succ_list.append((coord[0], coord[1]+1))
			succ_list.append((coord[0]+1, coord[1]))
			if coord[1]%2 == 0:
				succ_list.append((coord[0]-1, coord[1]-1))
				succ_list.append((coord[0]-1, coord[1]+1))
	
			elif coord[1]%2 == 1:	# odd lineparity
				succ_list.append((coord[0]+1, coord[1]-1))
				succ_list.append((coord[0]+1, coord[1]+1))
			
		# behaviour at the borders and corners:
		elif coord[0] == 0:	# left border
			if coord[1] == 0:	# upper left corner
				succ_list.append((0,1))
				succ_list.append((1,0))
			elif coord[1] == border:	# lower left corner
				if coord[1]%2 == 1:
					succ_list.append((coord[0]+1, coord[1]-1))
				succ_list.append((coord[0], coord[1]-1))
				succ_list.append((coord[0]+1, coord[1]))
			else:	# somewhere between y == 0 and y == border
				succ_list.append((coord[0], coord[1]-1))
				succ_list.append((coord[0], coord[1]+1))
				succ_list.append((coord[0]+1, coord[1]))
				if coord[1]%2 == 1:
					succ_list.append((coord[0]+1, coord[1]-1))
					succ_list.append((coord[0]+1, coord[1]+1))
		elif coord[1] == 0:		# upper border
			if coord[0] == border:	# upper right corner
				succ_list.append((coord[0]-1, 0))
				succ_list.append((coord[0]-1, 1))
				succ_list.append((coord[0], 1))
			else:	# somewhere between x == 0 and x == border
				succ_list.append((coord[0]-1, coord[1]))
				succ_list.append((coord[0], coord[1]+1))
				succ_list.append((coord[0]+1, coord[1]))
				succ_list.append((coord[0]-1, coord[1]+1))
		elif coord[0] == border:	# right border
			if coord[1] == border:	# lower right corner
				succ_list.append((coord[0]-1, coord[1]))
				succ_list.append((coord[0], coord[1]-1))
				if coord[1]%2 == 0:
					succ_list.append((coord[0]-1, coord[1]-1))
			else :	# somewhere between y == 0 and == border
				succ_list.append((coord[0]-1, coord[1]))
				succ_list.append((coord[0], coord[1]-1))
				succ_list.append((coord[0], coord[1]+1))
				if coord[1]%2 == 0:
					succ_list.append((coord[0]-1, coord[1]-1))
					succ_list.append((coord[0]-1, coord[1]+1))
		elif coord[1] == border:	# lower border
			# somewhere between x == 0 and x == border
			succ_list.append((coord[0]-1, coord[1]))
			succ_list.append((coord[0], coord[1]-1))
			succ_list.append((coord[0]+1, coord[1]))
			if coord[1]%2 == 0:
				succ_list.append((coord[0]-1, coord[1]-1))
			if coord[1]%2 == 1:
				succ_list.append((coord[0]+1, coord[1]-1))
			
		# deleting blocked nodes from the successorlist:
		temp_list = []	# cause removing items from lists over which you iterate is an bad idea
		for entry in succ_list:
			if self.obstacle_map[entry[0]][entry[1]] == True:
				temp_list.append(entry)
		for entry in temp_list:
			succ_list.remove(entry)
		return succ_list

	def _reconstruct_path(self, node):
		""" 
		Reconstructs the path to the given node from the start node
		(for which .pred is None) by using the predecessor reference 
		and finally reversing the order of the elements
		@param node the endnode at the path
		@return an iterator representing the path
		"""
		path = [node.coord]
		n = node
		while n.pred:
			n = n.pred
			path.append(n.coord)
		return reversed(path)
	
	def a_star(self, start, end):
		"""
		For simple testing at the console, for productive use take compute_path()
		"""
		self.obstacle_map = [[False, True, True, True, True, False, False], 
				[False, True, False, False, False, False, False], 
				[False, False, False, False, False, False ,False], 
				[True, True, True, True, True, True, True], 
				[False, False, False, False, False, False ,False], 
				[False, False, False, False, False, False ,False], 
				[False, False, False, False, False, False ,False]]
		path = self.compute_path(start, end)
		for node in path:
			print node

