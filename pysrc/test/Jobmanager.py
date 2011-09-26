#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
from Job import *
from BuildingRecipes import *
from SettlerRecipes import *

class Jobmanager:
	"""
	Manages all jobs for the carriers, graders, builders etc.
	There is an Jobmanagerinstance for every player.
	"""
	
	def __init__(self):
		"""
		Initializes the lists for the references of the units and the joblist.
		"""
		# maybe not necessary if there are lists anywhere else:
		self.carrier_number = 0
		self.grader_list = []
		self.builder_list = []
		self.jobless = []	# those who have a job, but no building
		
		self.jobs = []
		
		self.b_recipes = BuildingRecipes()
		self.s_recipes = SettlerRecipes()
		
		self._updateUnitList()


	def newJob(self, from_reference, to_do):
		"""
		Starts a new Job in its own thread. The Object calling this method must be the endpoint of the Job.
		@param from_reference: the reference of the object from which the job is
		@param to_do: what has to be done
		"""
		self._updateUnitList()
		self.jobs.append(Job(from_reference, to_do, self))
		self.jobs[len(jobs)-1].start()
		
	
	def clearJobList(self, jobreference):
		"""
		Removes calling job from the joblist.
		@param jobreference: the reference of the job to be canceled
		"""	
		if jobreference in self.jobs:
			self.jobs.remove(jobreference)
		else:
			raise ValueError("Wrong jobreference!")
			
		
			
	def _updateUnitList(self):
		"""
		"""
		pass
