#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
from Job import *

class Jobmanager:
	"""
	Manages all jobs for the carriers, graders, builders etc.
	There is an Jobmanagerinstance for every player.
	"""
	
	def __init__(self):
		"""
		Initializes the lists for the references of the units and the joblist.
		"""
		#self.carrier_list = []
		self.carrier_number = 0
		self.grader_list = []
		self.builder_list = []
		self.jobless = []	# those who have a job, but no building
		self.jobs = {}
		self.job_ID = 0

	def newJob(self, from_reference, to_do):
		"""
		Starts a new Job in its own thread. The Object calling this method must be the endpoint of the Job.
		@param from_reference the reference of the object from which the job is
		@param to_do what has to be done
		"""
		#TODO: joblist as a FIFO ???
		self.jobs[self.job_ID] = Job(self.job_ID, from_reference, to_do)
		self.jobs[self.job_ID].start()
		self.job_ID += 1
		
		
	def updateUnitList(self):
		pass
	
		
	def sendUnit(self):
		pass
