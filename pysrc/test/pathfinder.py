#!/usr/bin/env python
#-*- coding:utf-8 -*-

from path_heuristic import *
from priorityqueueset import PriorityQueueSet

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
		

def compute_path(start, end):
	"""
	Implements the A-Star algorithm (computes the path between start- and endpoint)
	The path is returned as an iterator to the points, 
	including the start- and endpoints themselves.
		
	If no path was found, an empty list is returned.
	
	TODO: sometimes not the direct path is chosen, if another has the same length
	"""
	sx = start[0]
	sy = start[1]
	ex = end[0]
	ey = end[1]
	closed_set = {}	# the set with the nodes along the path
	open_set = PriorityQueueSet()	# nodes which are possible for the path
	start_node = Node((sx, sy), 0, None)
	start_node.hcost = path_heuristic((sx, sy), (ex, ey))
	open_set.add(start_node)
	
	while len(open_set) > 0:
		curr_node = open_set.pop_smallest()
            
		if curr_node.coord == (ex, ey):
			return _reconstruct_path(curr_node)
		
		closed_set[curr_node] = curr_node
		
		for succ_coord in _successors(curr_node.coord):
			succ_node = Node(succ_coord)
			succ_node.gcost = curr_node.gcost + 1	# the cost from one node to another is always 1
			succ_node.hcost = path_heuristic(succ_node.coord, (ex, ey))
			
			if succ_node in closed_set:
				continue
				
			if open_set.add(succ_node):
				succ_node.pred = curr_node
				
	return []

def _successors(coord, border=8):
	"""
	Computes all successors of the given coord
	@param coord the coordinate whoms successors will be computed
	@param border x- and y-coordinate of the right and lower border
	@return a List with all successing nodes
	
	TODO: blocked nodes not implemented yet
		no error if coord is greater than border
	"""
	succ_list = []	# list with all possible successors of the given node
	
	if (coord[0] > 0 and coord[1] > 0) and (coord[0] < border and coord[1] < border):
		if coord[1]%2 == 0:
			succ_list.append((coord[0]-1, coord[1]-1))
			succ_list.append((coord[0]-1, coord[1]+1))
	
		elif coord[1]%2 == 1:	# odd lineparity
			succ_list.append((coord[0]+1, coord[1]-1))
			succ_list.append((coord[0]+1, coord[1]+1))
	
		succ_list.append((coord[0]-1, coord[1]))
		succ_list.append((coord[0], coord[1]-1))
		succ_list.append((coord[0], coord[1]+1))
		succ_list.append((coord[0]+1, coord[1]))
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
			if coord[1]%2 == 1:
				succ_list.append((coord[0]+1, coord[1]-1))
				succ_list.append((coord[0]+1, coord[1]+1))
			succ_list.append((coord[0], coord[1]-1))
			succ_list.append((coord[0], coord[1]+1))
			succ_list.append((coord[0]+1, coord[1]))
	elif coord[1] == 0:		# upper border
		if coord[0] == border:	# upper right corner
			succ_list.append((coord[0]-1, 0))
			succ_list.append((coord[0]-1, 1))
			succ_list.append((coord[0], 1))
		else:	# somewhere between x == 0 and x == border
			succ_list.append((coord[0]-1, coord[1]+1))
			succ_list.append((coord[0]-1, coord[1]))
			succ_list.append((coord[0], coord[1]+1))
			succ_list.append((coord[0]+1, coord[1]))
	elif coord[0] == border:	# right border
		if coord[1] == border:	# lower right corner
			if coord[1]%2 == 0:
				succ_list.append((coord[0]-1, coord[1]-1))
			succ_list.append((coord[0]-1, coord[1]))
			succ_list.append((coord[0], coord[1]-1))
		else :	# somewhere between y == 0 and == border
			if coord[1]%2 == 0:
				succ_list.append((coord[0]-1, coord[1]-1))
				succ_list.append((coord[0]-1, coord[1]+1))
			succ_list.append((coord[0]-1, coord[1]))
			succ_list.append((coord[0], coord[1]-1))
			succ_list.append((coord[0], coord[1]+1))
	elif coord[1] == border:	# lower border
		# somewhere between x == 0 and x == border
		if coord[1]%2 == 0:
			succ_list.append((coord[0]-1, coord[1]-1))
		if coord[1]%2 == 1:
			succ_list.append((coord[0]+1, coord[1]-1))
		succ_list.append((coord[0]-1, coord[1]))
		succ_list.append((coord[0], coord[1]-1))
		succ_list.append((coord[0]+1, coord[1]))
		
	return succ_list

def _reconstruct_path(node):
	""" 
	Reconstructs the path to the given node from the start node
	(for which .pred is None)
	"""
	path = [node.coord]
	n = node
	while n.pred:
		n = n.pred
		path.append(n.coord)
        return reversed(path)
	
def a_star(start, end):
	"""
	For simple testing at the console, not for productive use
	"""
	path = compute_path(start, end)
	for node in path:
		print node

