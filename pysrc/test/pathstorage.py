#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Pathstorage (object):

	def __init__(self):
		self.storage ={}	# the storage itself
		self.entries = 0	# the number of entries in the storage

	def add(self, path, replace=True):
		"""
		Adds a new path into the storage. Normally a path with the same key, but another
		value will overwrite an old one. Control this behaviour with the replace-switch.
		@param path the path to be stored (must be a non empty list of 2-tuples)
		@param replace by default this switch is true, which means newer pathes will
			replace older ones with the same key (start- and endpoint)
		"""		
		self.length1 = len(path) - 1
		
		if replace == True:
			self.storage[(path[0], path[self.length1])] = path
		else:	# otherwise the storage must be checked if there is the same key
			newkey = (path[0], path[self.length1])
			if newkey in self.storage.keys():
				pass	# if the newkey is already in the storage
			else:
				self.storage[newkey] = path
				
	def delete(self, path=None, pathkey=None):
		"""
		Removes a single path from the storage. If nothing is passed to this method,
		nothing will be deleted.
		@param path a hole path to be deleted
		@param pathkey the start- and endpoint of the path (must be a 2-tuple of 
			2-tuples) to be deleted
		"""
		if path == None and pathkey == None:
			pass
		elif pathkey != None:
			del self.storage[pathkey]
		else:
			self.length2 = len(path) - 1
			for key in self.storage:
				if key == (path[0], path[self.length2]):
					del self.storage[key]
					break
	
	def search_path(self, pathkey):
		"""
		Searches a path in the storage by its key, which is a tuple with the 
		start- and the endpoint of the path. The function also searches for reversed
		pathes.
		@param pathkey a 2-tuple of 2-tuples 
		@return returns either the path if it is in the storage or an empty list if not
		"""
		if pathkey in self.storage.keys():
			return self.storage[pathkey]
		if tuple(reversed(pathkey)) in self.storage.keys():
			return reversed(self.storage[tuple(reversed(pathkey))])
		else:
			return []
