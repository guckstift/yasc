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

		if to_do == "carry":
			self.carry()
		
		elif to_do == "grade":
			self.grade()
			
		elif to_do == "build":
			self.build()
			
		elif to_do == "learn a job":
			self.learnJob()
			
		elif to_do == "seize a building":	
			self.seizeBuilding()
			

	def carry(self):
		# carry sth. from A to B
		# search the thing to carry (as near as possible to B)
		# search a carrier near the thing to carry
		# send the carrier to the spot where the thing is
		# let him grab the thing
		# let him carry the thing to B
		pass
	
	def build(self):
		# build a building
		# search a number of builders near the building
		# send them to the building
		# let them build
		unit = self._searchUnit(self.endpoint, "builder")
		pass
	
	def grade(self):
		# grade an area for a building
		# search a number of graders near the area
		# send these units to the area
		# let them work
		unit = self._searchUnit(self.endpoint, "grader")
		pass
	
	def learnJob(self):
		#TODO: if no settler fits to the building to be seized, one settler has to learn the job
		# learn a job like lumberjack, butcher ... also for the soldier training
		pass
	
	def seizeBuilding(self):
		# civil and also military buildings
		# search a fitting settler near the building to be seized
		# send the unit to the building
		# associate him with the building
		# OR
		# search a settler with fitting occupation and associate him with the building
		pass
	
	
	def _searchUnit(self, coord, unit):
		"""
		Searches the nearest unit (to coord)
		@param coord: the coordinate from which the request comes, normally a building
		@param unit: what unit do you searching for?
		@return: the unit fitting the conditions
		"""
		#TODO: searching unit with floodfill algorithm?
		pass
		#return unit
	
	def _searchRessource(self, coord, ressource):
		"""
		Searches the nearest point (to coord) at which a ressource is laying.
		@param coord: the coordinate to which the ressource has to be transported
		@param ressource: which ressource has to be carried
		@return: a coord 
		"""
	
	def callbackPath(self, path):
		"""
		@param path: one/the path for this job.
		"""
		if path == None:
			print "Start- and endpoint not at the same island. No move possible."
		if ("go","on") in path:	# current path is only a part of the whole one
			pass
		elif ("end","point") in path:	# now this is the last part of the whole path
			pass
