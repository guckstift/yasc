#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PriorityQueueSet import PriorityQueueSet
from Pathstorage import *

class Pathfinder:
	"""
	The class organizing everything about pathfinding.
	@param pathstorage the storage with all computed pathes from actual gamesession
	@param macro_path_length optional parameter (default 4). Defines the length of the
	macro pathes. Must be even.
	
	Needs following files:
		priorityqueueset.py
		pathstorage.py
		
	TODO: 	*errormessage if coord is greater than border
		*sometimes not the direct path is chosen, if another one has the 
		same length
		*not storing reversed pathes
	"""

	def __init__(self, pathstorage, macro_path_length=4):
		if macro_path_length%2 != 0 or macro_path_length == 0:
			raise ValueError ("Bad macro_path_length!")
			
		self.macro_path_length = macro_path_length
		self.pathstorage = pathstorage

	def computePath(self, start, end):
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
		path = self.pathstorage.searchPath((start, end))
		if path != []:
			return path
		
		# if the path isn't stored, it will be calculated:
		sx = start[0]
		sy = start[1]
		ex = end[0]
		ey = end[1]
		closed_list = []	# the list with the nodes along the path
		open_set = PriorityQueueSet()	# nodes which are possible for the path
		step_size = 1	# the pathlength between node and his successors
		
		start_node = self._Node((sx, sy), 0, None)
		start_node.hcost = self.pathHeuristic((sx, sy), (ex, ey))
		open_set.add(start_node)
		
		if start_node.hcost > 2 * self.macro_path_length:
			step_size = self.macro_path_length
		
		succ_node = start_node
		
		while len(open_set) > 0:
			curr_node = open_set.popSmallest()
		    
			if (curr_node.coord == (ex, ey)) or (step_size > 1 and succ_node.hcost < step_size):
				path = self._reconstructPath(curr_node)
				# make a list from the iterator "path" (more handy):
				nodelist = []
				for entry in path:
					nodelist.append(entry)
	
				if step_size == 1:	
					self.pathstorage.add(nodelist)
					
					if end in nodelist:
						nodelist.append("end","point")	# last point in list is the endpoint
					else:
						nodelist.append("go","on")	# last pint in list isnt endpoint of the whole path but of a part of the macropath
				return nodelist	# a path was found
		
			closed_list.append(curr_node)

			for succ_coord in self.successors(curr_node.coord, step_size):
				succ_node = self._Node(succ_coord)
				succ_node.gcost = curr_node.gcost + 1	# the cost from one node to another is always 1
				succ_node.hcost = self.pathHeuristic(succ_node.coord, (ex, ey))
								
				if succ_node not in closed_list and open_set.add(succ_node):
					succ_node.pred = curr_node
				# if the node is in closed_list nothing is to do
				
		return []	# no path from start- to endpoint found
	
	def pathHeuristic(self, start, end):
		"""
		Calculates the distance of the shortest path between start- (sx,sy) and 
		endpoint (ex,ey).
		@param start a coordinat-tuple (x,y) of the startpoint
		@param end a coordinat-tuple (x,y) of the endpoint
		@return the minimal distance between the start- and endpoint
		"""
		sx = start[0] 	# the x-coordinate of the startpoint
		sy = start[1]	# the y-coordinate of the startpoint
		ex = end[0]	# the x-coordinate of the endpoint
		ey = end[1]	# the y-coordinate of the endpoint
	
		dx = abs(sx - ex)	# delta x - the distance in x-direction
		dy = abs(sy - ey)	# delta y - the distance in y-direction
	
		man_dist = dx + dy	# the manhattan-distance between start- and endpoint
	
		if sx == ex or sy == ey:
			return man_dist		# there are no diagonals at the shortes path
	
		# True if there is one (or more) diagonal like this: /. False if \:
		diagonal = (sx > ex and sy < ey ) or (sx < ex and sy > ey) 
	
		# vertical direction, True if endpoint is above the startpoint, False otherwise:
		vert_dir = (sy > ey)	
	
		# True if lineindex is odd, False otherwise:
		line_par = sy%2 == 1	
	
		if diagonal ^ vert_dir ^ line_par:
			max_diagonals = int((dy+1)/2)
		else:
			max_diagonals = int(dy/2)
	
		# max_diagonals is the maximum number of diagonals along the path from start to end
		return man_dist - min(dx, max_diagonals)


	def successors(self, coord, step_size=1):
		"""
		Computes all possible successors of the given coord
		@param coord the coordinate of which all successors will be computed
		@return a List with all successing nodes
		"""
		succ_list = []	# list with all possible successors of the given node
		
		n_x = (self.mapsize/2 + 1) - 1	# the right border (number of horizontal nodes -1)
		n_y = (self.mapsize + 1) - 1	# the lower border (number of vertical nodes -1)
		
		if step_size > 1:
			succ_list = self._macroSuccessors(coord, step_size, n_x, n_y)
		
		else:
			if 0 < coord[0] < n_x and 0 < coord[1] < n_y:
		
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
				
				elif coord[1] == n_y:	# lower left corner
			
					if coord[1]%2 == 1:
						succ_list.append((coord[0]+1, coord[1]-1))
					
					succ_list.append((coord[0], coord[1]-1))
					succ_list.append((coord[0]+1, coord[1]))
				
				else:	# somewhere between y == 0 and y == n_y
					succ_list.append((coord[0], coord[1]-1))
					succ_list.append((coord[0], coord[1]+1))
					succ_list.append((coord[0]+1, coord[1]))
				
					if coord[1]%2 == 1:
						succ_list.append((coord[0]+1, coord[1]-1))
						succ_list.append((coord[0]+1, coord[1]+1))
					
			elif coord[1] == 0:		# upper border
		
				if coord[0] == n_x:	# upper right corner
					succ_list.append((coord[0]-1, 0))
					succ_list.append((coord[0]-1, 1))
					succ_list.append((coord[0], 1))
				
				else:	# somewhere between x == 0 and x == n_x
					succ_list.append((coord[0]-1, coord[1]))
					succ_list.append((coord[0], coord[1]+1))
					succ_list.append((coord[0]+1, coord[1]))
					succ_list.append((coord[0]-1, coord[1]+1))
				
			elif coord[0] == n_x:	# right border
		
				if coord[1] == n_y:	# lower right corner
					succ_list.append((coord[0]-1, coord[1]))
					succ_list.append((coord[0], coord[1]-1))
				
					if coord[1]%2 == 0:
						succ_list.append((coord[0]-1, coord[1]-1))
					
				else :	# somewhere between y == 0 and == n_y
					succ_list.append((coord[0]-1, coord[1]))
					succ_list.append((coord[0], coord[1]-1))
					succ_list.append((coord[0], coord[1]+1))
				
					if coord[1]%2 == 0:
						succ_list.append((coord[0]-1, coord[1]-1))
						succ_list.append((coord[0]-1, coord[1]+1))
					
			elif coord[1] == n_y:	# lower border
		
				# somewhere between x == 0 and x == n_x
				succ_list.append((coord[0]-1, coord[1]))
				succ_list.append((coord[0], coord[1]-1))
				succ_list.append((coord[0]+1, coord[1]))
			
				if coord[1]%2 == 0:
					succ_list.append((coord[0]-1, coord[1]-1))
				
				if coord[1]%2 == 1:
					succ_list.append((coord[0]+1, coord[1]-1))
			
		# deleting blocked nodes from the successorlist:
		temp_list = []	# cause removing items from lists over which you iterate is an bad idea
		# no obstaclemap for testing
		"""
		#print "Koordinate {0}:".format(coord)
		#print succ_list
		for entry in succ_list:	# fill temp_list with blocked nodes
			if self.obstacle_map[entry[1]][entry[0]] == True:
				#print "kicked entry: {0}".format(entry)
				temp_list.append(entry)
				
		for entry in temp_list:	# remove all nodes in temp_list from succ_list
			succ_list.remove(entry)
		"""	
		#print succ_list
		return succ_list
	
	def _macroSuccessors(self, coord, step_size, n_x, n_y):
		"""
		Computes all possible successors of coord with the given stepsize. This is
		only for steps greater than 1.
		@param coord the coordinate for witch the successors will be computed
		@param step_size the stepsize
		@param n_x the maximal x-coordinate
		@param n_y the maximal y-coordinate
		"""
		macro_succ_list = []
		
		half_ss = step_size/2
		
		if half_ss <= coord[0] <= n_x-half_ss and step_size <= coord[1] <= n_y-step_size:
			macro_succ_list.append((coord[0] - step_size, coord[1]))
			macro_succ_list.append((coord[0] + step_size, coord[1]))
			macro_succ_list.append((coord[0] - half_ss, coord[1] - step_size))
			macro_succ_list.append((coord[0] + half_ss, coord[1] - step_size))
			macro_succ_list.append((coord[0] - half_ss, coord[1] + step_size))
			macro_succ_list.append((coord[0] + half_ss, coord[1] + step_size))
		
		elif 0 <= coord[0] < half_ss:	# left border
			if 0 <= coord[1] < step_size:	# upper left corner
				macro_succ_list.append((coord[0] + step_size, coord[1]))
				macro_succ_list.append((coord[0] + half_ss, coord[1] + step_size))
	
			elif step_size < coord[1] <= n_y: 	# lower left corner
				macro_succ_list.append((coord[0] + half_ss, coord[1] - step_size))
				macro_succ_list.append((coord[0] + step_size, coord[1]))
	
			else:
				macro_succ_list.append((coord[0] + half_ss, coord[1] - step_size))
				macro_succ_list.append((coord[0] + step_size, coord[1]))
				macro_succ_list.append((coord[0] + half_ss, coord[1] + step_size))
				
		elif 0 <= coord[1] < step_size:	# upper border
			if n_x-half_ss < coord[0] <= n_x:	# upper right corner
				macro_succ_list.append((coord[0] - step_size, coord[1]))
				macro_succ_list.append((coord[0] - half_ss, coord[1] + step_size))
				
			else:
				macro_succ_list.append((coord[0] - step_size, coord[1]))
				macro_succ_list.append((coord[0] + step_size, coord[1]))
				macro_succ_list.append((coord[0] - half_ss, coord[1] + step_size))
				macro_succ_list.append((coord[0] + half_ss, coord[1] + step_size))
				
		elif n_x-half_ss < coord[0] <= n_x:	# right border
			if n_y-step_size < coord[1] <= n_y:	# lower right corner
				macro_succ_list.append((coord[0] - step_size, coord[1]))
				macro_succ_list.append((coord[0] - half_ss, coord[1] - step_size))
				
			else:
				macro_succ_list.append((coord[0] - half_ss, coord[1] + step_size))
				macro_succ_list.append((coord[0] - step_size, coord[1]))
				macro_succ_list.append((coord[0] - half_ss, coord[1] - step_size))
				
		elif n_y-step_size < coord[1] <= n_y:	# lower border
			macro_succ_list.append((coord[0] - step_size, coord[1]))
			macro_succ_list.append((coord[0] + step_size, coord[1]))
			macro_succ_list.append((coord[0] - half_ss, coord[1] - step_size))
			macro_succ_list.append((coord[0] + half_ss, coord[1] - step_size))
			
		# deleting blocked nodes from the successorlist:
		temp_list = []
		# no obstaclemap for testing
		"""
		#print "Koordinate {0}:".format(coord)
		#print succ_list
		for entry in succ_list:	# fill temp_list with blocked nodes
			if self.obstacle_map[entry[1]][entry[0]] == True:
				#print "kicked entry: {0}".format(entry)
				temp_list.append(entry)
				
		for entry in temp_list:	# remove all nodes in temp_list from succ_list
			succ_list.remove(entry)
		"""	
		return macro_succ_list

	def _reconstructPath(self, node):
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
	
	def aStar(self, start, end, obstacle_map):
		"""
		The entrymethod for pathfinding.
		@param start the startnode
		@param end the endnode
		@param obstacle_map the array of rows with a boolean for every node if it 
		is blocked. Every row is an array itself.
		"""
		#if obstacle_map == None:
		#	self.obstacle_map = [[False, True, True, True], 
		#			[False, True, False, False], 
		#			[False, False, False, False], 
		#			[True, True, True, True],
		#			[False, False, False, False],
		#			[False, True, False, False],
		#			[False, False, False, False]]
		#else:
		self.obstacle_map = obstacle_map
		
		self.mapsize = len(self.obstacle_map) - 1	# the size of the map in triangles
		self.mapsize = 1000
		path = self.computePath(start, end)
			
		return path
		
		
	class _Node:
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
			return cmp(self.getFcost(), other.getFcost())
		
		def __hash__(self):
			return hash(self.coord)
				
		def getFcost(self):
			"""
			Returns the cost f(x) of this node. Its the sum of g(x) and h(x)
			"""
			return self.gcost + self.hcost

