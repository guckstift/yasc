
from display import *
from terrainset import *
from vertexarray import *
from constants import *
from surface import *
from sprite import *

class GFXEngine :

	"""
	This class draws the gfx
	"""

	def __init__ (self, lll, display, viewspace, mymap):
	
		self.lll = lll
		self.display = display
		self.viewspace = viewspace
		self.mymap = mymap
		self.terrainset = Terrainset ()
		
		# Test
		self.settsurf = Surface ()
		self.settsurf.loadFromFile ("gfx/protosettler.png")
		self.settsurf.cols = 16
		self.settsurf.rows = 16
		self.sett = Sprite (self.viewspace, self.settsurf)
		self.sett.x = 100
		self.sett.y = 100
		self.sett.configAnimation (True, 0, 24, 0, 25)
	
	def tick (self):
	
		self.display.clear ()
		self.draw ()
		self.sett.drawToDisplay (self.display)
		self.display.showFrame ()

	def draw (self):
	
		self.drawLandscape ()
	
	def drawLandscape (self):
	
		self.drawTerrain ()

	def drawTerrain (self):
	
		self.lll.view.GFXEngineSDLOGL_DrawTerrain (self.mymap.terra.asCArray (),
			self.mymap.mapsize, TRIA_W, TRIA_H,
			TEX_FACTOR, self.terrainset.asCArray(), self.mymap.getVertarray().asCArray())
