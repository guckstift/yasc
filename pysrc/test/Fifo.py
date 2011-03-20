#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Fifo:
	"""
	A typical FIFO buffer.
	"""

	def __init__(self):
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
	
	def somethingIn(self):
		"""
		For notifying that there is something to pop.
		"""
		pass

