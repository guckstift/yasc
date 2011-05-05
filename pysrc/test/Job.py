#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Job(threading.Thread):
	"""
	Represents a single Job started by the Jobmanager. Every Job runs in its own thread.
	The possibility to search for more than one unit is not implemented yet.
	"""

	def __init__(self, ID, from_reference, to_do):
		"""
		"""
		self.ID = ID
		self.from_reference = from_reference
		self.to_do = to_do

	def run(self):
		"""
		Overwrites the basic run()-method of the threading-module.
		"""
		self.endpoint = self.from_reference.coord	# the endpoint of every job is the thing ordering this job

		if to_do == "carry":	# carry sth. from A to B
			pass
		elif to_do == "grade":	# grade an area for a building
			unit = self.searchUnit(self.endpoint, "grader")
			
		elif to_do == "build":	# build a building
			unit = self.searchUnit(self.endpoint, "builder")
		#TODO: if no settler fits to the building to be seized, one settler has to learn the job
		elif to_do == "learn a job":	# learn a job like lumberjack, butcher ... also for the soldier training
			pass
		elif to_do == "seize a building":	# civil and also military buildings
			pass

	def searchUnit(self, coord, unit):
		"""
		@param coord the coordinate from which the request comes, normally a building
		@param unit what unit do you searching for?
		@return the unit fitting the conditions
		"""
		#TODO: searching unit with floodfill algorithm?
		pass
		#return unit
	
	def callbackPath(self, path):
		"""
		@param path one/the path for this job.
		"""
		if path == None:
			print "Start- and endpoint not at the same island. No move possible."
		if ("go","on") in path:	# current path is only a part of the whole one
			pass
		elif ("end","point") in path:	# now this is the last part of the whole path
			pass
