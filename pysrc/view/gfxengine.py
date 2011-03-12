
import ctypes as ct

TRIA_W = 28
TRIA_H = 14
HEIGHT_UNIT_PX = 8

TERRAIN_PNG_DIR = "gfx/terrain"
TERRAIN_TEXTURE_FILES = ["grass.png"]
TEX_FACTOR = 8

class GFXEngine :

	"""
	The generic GFX-Engine of yasc. Should be subclassed to implement technology-dependent
	Drawing-methods.
	"""

	def __init__ (self, display=None, view=None, mymap=None) :
	
		self.SetDisplay (display)
		self.SetView (view)
		self.SetMap (mymap)
		self.LoadTerrainset ()
	
	def LoadTerrainset (self) :
	
		"""
		This loads the Terrainset from files and prepares it.
		automatically called by the constructor.
		"""
	
		self.terrainset = []

	def Draw (self) :
	
		self.DrawLandscape ()
		
	def DrawLandscape (self) :
		
		self.DrawTerrain ()
		
	def DrawTerrain (self) :
	
		"""
		Draws triangles and borders, where 2 different terrains border on each other.
		[override me]
		"""
	
		pass
		
	def SetDisplay (self, display) :
		
		self.display = display
		
	def SetView (self, view) :
		
		self.view = view
		
	def SetMap (self, mymap) :
		
		self.mymap = mymap
		self.vertarr = Vertexarray (mymap)

class Vertexarray :

	"""
	This class supplies an array of 2D-vertices of a given map (currently only as 3D-c-types-array)
	"""
	
	def __init__ (self, mymap):
	
		self.mymap = mymap
		self.carr = None
	
	def asCArray (self):

		if self.carr == None:

			INT = ct.c_int
			PINT = ct.POINTER(INT)
			PPINT = ct.POINTER(PINT)
			POINT = INT * 2
			VERTLINE = PINT * self.mymap.heights.vwi
			VERTMAP = PPINT * self.mymap.heights.vhe
			self.carr = VERTMAP ()
			for y in range(self.mymap.heights.vhe):
				self.carr[y] = VERTLINE ()
				for x in range(self.mymap.heights.vwi):
					self.carr[y][x] = POINT ()
					self.carr[y][x][0], self.carr[y][x][1] = (
						x*TRIA_W + TRIA_W/2*(y%2), y*TRIA_H - self.mymap.heights.data[y][x]*HEIGHT_UNIT_PX)
		
		return self.carr
	
	def updateFromMap (self):
	
		for y in range(self.mymap.heights.vhe):
			for x in range(self.mymap.heights.vwi):
				self.carr[y][x][0], self.carr[y][x][1], self.carr[y][x][2] = (
					x*TRIA_W + TRIA_W/2*(y%2), y*TRIA_H - self.mymap.heights.data[y][x]*HEIGHT_UNIT_PX)


