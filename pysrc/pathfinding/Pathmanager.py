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
	There is one Pathmanager per match. He cares about all pathrequest from all players.
	# TODO: ObstacleMap
	"""
	
	def __init__(self):
		self.pathstorage = Pathstorage()
		self.obstacle_map = [[]]
		self.fifo = Fifo(self)
		self.islands = Islands()
		self.jobs = {}	# contains all pathfindingjobs
		self.job_ID = 0 # the ID for a pathfindingjob - must be unique
		
	def addJob(self, reference, start, end):
		"""
		@param reference the reference of the instance of the settler who needs the path
		@param start the startnode
		@param end the endnode
		"""
		#TODO: there will be a problem if finished jobs where not deleted from list
		self.jobs[self.job_ID] = threading.Thread(target = self.findPath, name=self.job_ID, args=(reference,start,end))
		self.jobs[self.job_ID].start()
		self.job_ID += 1

	def cancelJob(self, job_ID):
		"""
		Cancels job if for example unit doesnt exist any longer.
		@param job_ID the ID which is the name of the thread and the ID in the set of jobs
		"""
		#TODO. how to kill single threads?
		pass

	def returnJob(self):
		"""
		Returns a path to the unit. Called by the FIFO.
		"""
		while not self.fifo.isEmpty():
			job = self.fifo.pop()
			#print job
			reference = job.keys()
			reference.callbackPath(job[reference])
		#pass

	def findPath(self, reference, start, end):
		"""
		Start computing the Path.
		@param reference the reference of the settler who needs the path
		@param start the startnode
		@param end the endnode
		"""
		
		if self.islands.sameIsland(start, end):
			pf = Pathfinder(self.pathstorage)
			lock = threading.Lock()
			# computing the (macro)path:
			path = pf.aStar(start, end, None)	# obstaclemap is None for testing
			
			# TODO: if both nodes are at the same island, there should be a path every time
			
			# if a macropath was computed:
			if abs(path[0][0] - path[1][0]) > 1 or abs(path[0][1] - path[1][1]) > 1:
				macro_path = path
				last_index = len(path) - 1
				#path = []
				i = 0	# only every second node of the macro path is used
				
				for node in macro_path:
					if i%2 == 0 and i+2 < last_index:
						temp_path = pf.aStar(node, macro_path[i+2], None)
						lock.acquire()	# because only one thread should access the one FIFO
						self.fifo.add(reference, temp_path)
						lock.release()
						#print temp_path
						#for item in temp_path:
						#	path.append(item)
						time.sleep(2)
						
					elif i%2 == 0:	# endnode is closer than one macrostep
						temp_path = pf.aStar(node, end, None)
						lock.acquire()
						self.fifo.add(reference, temp_path)
						lock.release()
						#print temp_path
						#for item in temp_path:
						#	path.append(item)
						break
						
					i = i + 1
			else:	# its a short path (no macropath needed)
				lock.acquire()
				self.fifo.add(reference, path)
				lock.release()
				
		else:	# start- and endpoint not at the same island - no path can be computed
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
		Be up to date. Checks every node wheather it is blocked (permanently, not by units) or not.
		"""
		pass
		
		# simple test if the number of triangles horizontally and vertically are the same:
		#size_test = len(self.obstacle_map) - 1
		#if size_test != (len(self.obstacle_map[0]) - 1) * 2:
		#	raise ValueError ("Bad obstacle_map!")
		#	return -1

