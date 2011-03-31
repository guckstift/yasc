
from Display import *
from TerrainSet import *
#from VertexArray import *
from constants import *
from Surface import *
from Sprite import *

class GFXEngine :

	"""
	This class draws the gfx
	"""

	def __init__ (self, lll, viewspace, mymap):
	
		self.lll = lll
		self.display = Display ()
		self.viewspace = viewspace
		self.mymap = mymap
		self.terrainset = TerrainSet ()
		
		# Test
		self.settsurf = Surface ()
		self.settsurf.loadFromFile ("gfx/protosettler.png")
		self.settsurf.cols = 16
		self.settsurf.rows = 16
		self.sett = Sprite (self.viewspace, self.settsurf)
		self.sett.x = 100
		self.sett.y = 100
		self.sett.configAnimation (True, 0, 24, 25)
	
	def tick (self):
	
		"""
		tick() executes all actions which must be done by the GFX-Engine in one Game-Loop-cycle
		This is: clearing the screen, drawing all objects, showing the new game-frame
		"""
	
		self.display.clear ()
		self.draw ()
		self.sett.drawToDisplay (self.display)
		self.display.showFrame ()

	def draw (self):
	
		self.drawLandscape ()
	
	def drawLandscape (self):
	
		self.drawTerrain ()

	def drawTerrain (self):
	
		self.lll.view.DrawTerrain (self.mymap.terra.asCArray (), self.mymap.mapsize, TRIA_W, TRIA_H,
			TEX_FACTOR, self.terrainset.asCArray(), self.mymap.getVertarray().asCArray())


