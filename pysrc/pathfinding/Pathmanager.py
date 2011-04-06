#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Pathstorage import *
from Pathfinder import *
from Fifo import *
from Islands import *
import threading
import time

class Pathmanager:
	"""
	Organizes the pathfinding. Can start serveral threads, realizes the two-tiered
	pathfinding, cares about the obstaclemap ...
	# TODO: ObstacleMap
	"""
	
	def __init__(self):
		self.pathstorage = Pathstorage()
		self.obstacle_map = [[]]
		self.fifo = Fifo(self)
		self.islands = Islands()
		
	def addJob(self, reference, start, end):
		"""
		@param reference the reference of the instance of the settler who needs the path
		@param start the startnode
		@param end the endnode
		"""
		th = threading.Thread(target = self.findPath, name=reference, args=(reference,start,end))
		th.start()

	def cancelJob(self, reference):
		"""
		Cancels job if for example unit doesnt exist any longer.
		"""
		#TODO. how to kill single threads?
		pass

	def returnJob(self):
		"""
		Returns a path to the unit asking for it.
		@param reference the reference of the instance asking for the path
		@param path the path for the unit
		"""
		#while not self.fifo.isEmpty()
			#job = self.fifo.pop()
			#reference = job.keys()
			#reference.callbackPath(job[reference])
		pass

	def findPath(self, reference, start, end):
		"""
		Start the computing of the Path.
		@param reference the reference of the settler who needs the path
		@param start the startnode
		@param end the endnode
		"""
		
		if self.islands.sameIsland(start, end):
			pf = Pathfinder(self.pathstorage)
			lock = threading.Lock()
			
			path = pf.aStar(start, end, None)	# obstaclemap is None for testing
			last_index = len(path) - 1
		
		else:
			path = []	# start- and endpoint not at the same island
		
		
		if path != []:	# TODO: if both nodes are at the same island, there should be a path every time
			if abs(path[0][0] - path[1][0]) > 1 or abs(path[0][1] - path[1][1]) > 1:
				# macro path was computed
				macro_path = path
				path = []
				i = 0	# only every second node of the macro path is used
				
				for node in macro_path:
					if i%2 == 0 and i+2 < last_index:
						temp_path = pf.aStar(node, macro_path[i+2], None)
						lock.acquire()	# because only one thread should access the one fifo
						self.fifo.add(reference, temp_path)
						lock.release()
						#print temp_path
						for item in temp_path:
							path.append(item)
						time.sleep(2)
						
					elif i%2 == 0:	# endnode is closer than one macrostep
						temp_path = pf.aStar(node, end, None)
						lock.acquire()
						self.fifo.add(reference, temp_path)
						lock.release()
						#print temp_path
						for item in temp_path:
							path.append(item)
						break
						
					i = i + 1
			else:
				lock.acquire()
				self.fifo.add(reference, path)
				lock.release()
		else:
			lock.acquire()
			self.fifo.add(reference, None)
			lock.release()
		#print path
		
	def findIslands(self):
		"""
		Let the class Islands find and store islands.
		"""
		#self.updateObstaclemap()
		self.islands.searchIslands(self.obstacle_map)
	
	def updateObstaclemap(self):
		"""
		Be up to date.
		"""
		pass
		
		# simple test if the number of triangles horizontally and vertically are the same:
		#size_test = len(self.obstacle_map) - 1
		#if size_test != (len(self.obstacle_map[0]) - 1) * 2:
		#	raise ValueError ("Bad obstacle_map!")
		#	return -1

