#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Pathstorage import *
from Pathfinder import *
from Fifo import *
import threading
import time

class Pathmanager:
	"""
	Organizes the pathfinding. Can start serveral threads, realizes the two-tiered
	pathfinding, cares about the obstaclemap ...
	"""
	
	def __init__(self):
		self.pathstorage = Pathstorage()
		self.obstacle_map = [[]]
		self.fifo = Fifo()
		
	def addJob(self, ID, start, end):
		"""
		@param ID
		@param start the startnode
		@param end the endnode
		"""
		th = threading.Thread(target = self.findPath, name=ID, args=(ID,start,end))
		th.start()
		

	def findPath(self, ID, start, end):
		"""
		Start the computing of the Path.
		@param ID
		@param start the startnode
		@param end the endnode
		"""
		pf = Pathfinder(self.pathstorage)
		
		path = pf.aStar(start, end, None)	# obstaclemap is None for testing
		last_index = len(path) - 1
		
		if path != []:
			if abs(path[0][0] - path[1][0]) > 1 or abs(path[0][1] - path[1][1]) > 1:
				# macro path was computed
				macro_path = path
				path = []
				i = 0	# only every second node of the macro path is used
				
				for node in macro_path:
					if i%2 == 0 and i+2 < last_index:
						temp_path = pf.aStar(node, macro_path[i+2], None)
						self.fifo.add(ID, temp_path)
						#print temp_path
						for item in temp_path:
							path.append(item)
						time.sleep(2)
						
					elif i%2 == 0:	# now its really hot ;)
						temp_path = pf.aStar(node, end, None)
						self.fifo.add(ID, temp_path)
						#print temp_path
						for item in temp_path:
							path.append(item)
						break
						
					i = i + 1
			else:
				self.fifo.add(ID, path)
		else:
			self.fifo.add(ID, None)
		#print path
	
	def updateObstaclemap(self):
		"""
		"""
		pass
		
		# simple test if the number of triangles horizontally and vertically are the same:
		#size_test = len(self.obstacle_map) - 1
		#if size_test != (len(self.obstacle_map[0]) - 1) * 2:
		#	raise ValueError ("Bad obstacle_map!")
		#	return -1

