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
		self.endpoint = self.from_reference.coord

		if to_do == "carry":	# carry sth. from A to B
			pass
		elif to_do == "grade":	# grade an area for a building
			unit = self.searchUnit(self.endpoint)
			
		elif to_do == "build":	# build a building
			pass
		#TODO: if no settler fits to the building to be seized, one settler has to learn the job
		elif to_do == "learn a job":	# learn a job like lumberjack, butcher ... also for the soldier training
			pass
		elif to_do == "seize a building":	# civil and also military buildings
			pass

	def searchUnit(self, coord):
		"""
		@param coord the coordinate from which the request comes, normally a building
		"""
		#TODO: searching unit with floodfill algorithm?
		pass
