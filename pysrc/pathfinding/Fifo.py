#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Fifo:
	"""
	A typical FIFO buffer.
	@param pathmanager the instance of the pathmanager initialising this fifo
	"""

	def __init__(self, pathmanager):
		self.pathmanager = pathmanager 	# the instance of the pathmanager
		self.fifo = []
		
	def add(self, ID, path):
		"""
		Adds a new dictionary at the end of the list.
		"""
		entry = {ID: path}
		self.fifo.append(entry)
		
		if len(self.fifo) == 1:
			self.somethingIn()
		
	def pop(self):
		"""
		Pops the oldest element of the list. Or None if nothing is in.
		"""
		if self.fifo != []:
			return self.fifo.pop(0)
		return None

	def isEmpty(self):
		"""
		Return True if the fifo is empty. False otherwise
		"""
		if self.fifo == []:
			return True
		return False
	
	def somethingIn(self):
		"""
		For notifying that there is something to pop.
		"""
		self.pathmanager.returnJob()
		pass

