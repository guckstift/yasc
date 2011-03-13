
import time
from sdl import *

from lowlevel import *
from view import *
from game import *

ll = LowLevelLib ()
display = DisplaySDLOGL ()
viewp = Viewpoint ()
mymap = Map (40)
mymap.heights.setHeight(2,3,-1)
mymap.heights.setHeight(2,5,1)
mymap.heights.setHeight(4,5,-1)
gfxengine = GFXEngineSDLOGL (ll, display, viewp, mymap)

settsurf = SurfaceSDLOGL ()
settsurf.LoadFromFile ("gfx/protosettler.png")
settsurf.cols = 16
settsurf.rows = 16
sett = Sprite (display, viewp, settsurf)
sett.ConfigAnimation (True, 0, 24, 0, 50)

frames = 0
lasttick = SDL_GetTicks ()

running = True
while running :

	while SDL_PollEvent() :
	
		event = SDL_PollEventAndReturn ()
		if event.type == SDL_KEYDOWN :
			running = False
		elif event.type == SDL_QUIT :
			running = False
			
	display.Clear()
	
	framestart = SDL_GetTicks ()
	
	gfxengine.Draw()
	#settsurf.DrawToDisplay (display,100,100,0)
	sett.DrawMe ()

	display.ShowFrame ()
	
	frames += 1
	if SDL_GetTicks()-lasttick >= 1000:
		print str(frames)+" fps"+(" - below 40 fps :-( !" if frames<40 else "")
		frames = 0
		lasttick = SDL_GetTicks ()
	
	#time.sleep (0.02)
	
	## enable this to see how long the whole drawing-procedure takes for each frame in milliseconds
	#framelen = SDL_GetTicks () - framestart
	#print str(framelen) + " ms " + (" - exceeded 20 ms" if framelen>20 else "")

