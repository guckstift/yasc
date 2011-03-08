#!/usr/bin/env python

TRIA_W = 28
TRIA_H = 14

TERRAIN_PNG_DIR = "gfx/terrain"
TERRAIN_TEXTURE_FILES = ["grass.png"]
TEX_FACTOR = 8

class GFXEngine :

	def __init__ (self, display=None, view=None, mymap=None) :
	
		self.SetDisplay (display)
		self.SetView (view)
		self.SetMap (mymap)
		self.LoadTerrainset ()
	
	def LoadTerrainset (self) :
	
		self.terrainset = []

	def Draw (self) :
	
		self.DrawLandscape ()
		
	def DrawLandscape (self) :
		
		self.DrawTerrain ()
		
	def DrawTerrain (self) :
	
		# Draw Triangles
		for y in range(self.mymap.mapsize):
			for x in range(self.mymap.mapsize):
				self.DrawTriangle (x, y, (x+y)%2 == 1)
		# Draw Borders
		
	def DrawTriangle (self, x, y, upt=False) :
		"""
		@param x, y: triangle address
		"""
		
		pass
		
	def DrawBorder (self) :

		pass
		
	def SetDisplay (self, display) :
		
		self.display = display
		
	def SetView (self, view) :
		
		self.view = view
		
	def SetMap (self, mymap) :
		
		self.mymap = mymap

