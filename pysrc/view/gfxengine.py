
TRIA_W = 28
TRIA_H = 14

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

