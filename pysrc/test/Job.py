#!/usr/bin/env python
#-*- coding:utf-8 -*-

import string
import threading

class Job(threading.Thread):
	"""
	Represents a single Job started by the Jobmanager. Every Job runs in its own thread.
	The possibility to search for more than one unit is not implemented yet.
	"""

	def __init__(self, from_reference, to_do, manager_reference):
		"""
		@param from_reference: the reference of the object needing this job
		@param to_do: what to do. Contains single word like "grade" or two words like "carry wood".
		@param manager_reference: the reference of the manager managing all jobs
		"""
		threading.Thread.__init__(self)
		self.from_reference = from_reference
		self.to_do = to_do
		self.manager_reference = manager_reference
		self.lock = threading.Lock()
		

	def run(self):
		"""
		Overwrites the basic run()-method of the threading-module.
		"""
		self.endpoint = self.from_reference.coord	# the endpoint of every job is the thing ordering this job

		if "carry" in self.to_do:
			self._carry()			
		elif self.to_do == "grade":	
			self._grade()			
		elif self.to_do == "build":	
			self._build()			
		elif "learn" in self.to_do:	
			self._learn()			
		elif "seize" in self.to_do:	
			self._seize()


	def _carry(self):
		"""
		Carry sth. from A to B
		"""
		unit = self._searchUnitOrWare(self.endpoint, "unit", "carrier")
		_ware_name = string.split(self.to_do)[1]
		ware = self._searchUnitOrWare(unit.coord, "ware", _ware_name)
		#TODO: send carrier to ware let him take it and send him to the endpoint
		self.lock.acquire()
		self.manager_reference.clearJobList(self)
		self.lock.release()
		
		
	def _grade(self):
		"""
		Grade an area for a building
		"""
		unit = self._searchUnitOrWare(self.endpoint, "unit", "grader")
		#TODO: send grader to endpoint and let him grade the construction area
		self.lock.acquire()
		self.manager_reference.clearJobList(self)
		self.lock.release()		
		
		
	def _build(self):
		"""
		Build a building
		"""
		unit = self._searchUnitOrWare(self.endpoint, "unit", "builder")
		#TODO: send builder to endpoint and let him build the building
		self.lock.acquire()
		self.manager_reference.clearJobList(self)
		self.lock.release()		
		
		
	def _learn(self):
		"""
		Learn a job like lumberjack, butcher ... also for the soldier training 
		"""
		#TODO: at the moment not for military units
		_job_name = string.split(self.to_do)[1]
		_tool = self.manager_reference.s_recipes[_job_name]
		
		if _tool is not None:
			ware = self._searchUnitOrWare(self.endpoint, "ware", _tool)
			unit = self._searchUnitOrWare(ware.coord, "unit", "settler")
			#TODO: send settler to tool and change his job
		else:
			unit = self._searchUnitOrWare(self.endpoint, "unit", "settler")
			#TODO: change job
		#TODO: wake calling Job (to seize a building)
		self.lock.acquire()
		self.manager_reference.clearJobList(self)
		self.lock.release()		
		
		
	def _seize(self):
		"""
		Civil and also military buildings
		"""
		_unit_name = string.split(self.to_do)[1]
		unit = self._searchUnit(self.endpoint, "unit", _unit_name)
		if unit == None:	# only for non-military units
			self.manager_reference.newJob(self.endpoint, "learn " + _unit_name)
			# let this job wait until unit is ready
		#TODO: send unit to building and let him seize it
		self.lock.acquire()
		self.manager_reference.clearJobList(self)
		self.lock.release()		
		
		
	def _searchUnitOrWare(self, coord, unit_ware, search_for):
		"""
		@param coord: the coordinate from which the request comes, normally a building
		@param unit_ware: contains "unit" if a unit is wanted; "ware" otherwise
		@param search_for: what unit or ware to search for
		@return: the unit/ware (reference) closest to coord or None if none is available
		"""
		#TODO: get a warelist!
		#TODO: test ware- and settlerlist if they contain the thing you searching for
		old_dist = 999999999
		if unit_ware ==  "unit":
			#TODO: test settlerlist
			#for entry in se
			pass
			
		elif unit_ware == "ware":
			#TODO: test warelist
			for entry in warelist:		# search the hole warelist
				new_dist = _calcDistance(coord, entry.coord)
				if new_dist <= 1:	# break the search 
					return entry
				if new_dist < old_dist:	# if new ware is closer to coord, take this
					old_dist = new_dist
					closest_entry = entry
			return closest_entry
		
		raise ValueError ("Variable 'unit_ware' must be either 'unit' or 'ware'!")
		
	
	def _calcDistance(self, start, end):
		"""
		Calculates the distance between start- (sx,sy) and endpoint (ex,ey).
		@param start: a coordinat-tuple (x,y) of the startpoint
		@param end: a coordinat-tuple (x,y) of the endpoint
		@return: the minimal distance between the start- and endpoint
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
	
	
	def _callbackPath(self, path):
		"""
		@param path: one/the path for this job.
		"""
		if path == None:
			print "Start- and endpoint not at the same island. No move possible."
		if ("go","on") in path:	# current path is only a part of the whole one
			pass
		elif ("end","point") in path:	# now this is the last part of the whole path
			pass
