#!/usr/bin/env python

import ctypes

class Map :

	def __init__ (self, mapsize=8):
	
		if mapsize<2 or mapsize%2 == 1:
			raise Exception("Mapsize to small!")
		
		self.mapsize = mapsize # kartenbreite und kartenhoehe
		self.vwi = 1+(self.mapsize/2) # vertices per line
		self.vhe = self.mapsize+1 # vertex-line-count
		self.terrmap = [[0 for x in range(mapsize)] for y in range(mapsize)] # terrain-type of polys
		self.hmap = [[0 for x in range(self.vwi)] for y in range(self.vhe)] # hights of vertices
	
	def setTria (self, x, y, terra) :
	
		self.terrmap[y][x] = terra
	
	def setHight (self, x, y, h) :

		self.hmap[y][x] = h
	
	def terrAsCarray (self):
		
		intarr = ctypes.c_uint * self.mapsize
		intarrarr = intarr * self.mapsize
		
		res = intarrarr()
		for y in range(self.mapsize) :
			for x in range(self.mapsize) :
				res[y][x] = self.terrmap[y][x]
		# TO DO: improve this to return a pointer to line-pointers to line-arrays

		return res

