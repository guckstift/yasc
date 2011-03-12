
from sdl import *

from lowlevel import *
from view import *
from game import *

ll = LowLevelLib ()
display = DisplaySDLOGL ()
view = View ()
mymap = Map (40)
mymap.heights.setHeight(2,3,-1)
mymap.heights.setHeight(2,5,1)
mymap.heights.setHeight(4,5,-1)
gfxengine = GFXEngineSDLOGL (ll, display, view, mymap)

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
		
	display.ShowFrame ()
	
	frames += 1
	if SDL_GetTicks()-lasttick >= 1000:
		print str(frames)+" fps"
		frames = 0
		lasttick = SDL_GetTicks ()
	
	## enable this to see how long the whole drawing-procedure takes for each frame in milliseconds
	#framelen = SDL_GetTicks () - framestart
	#print str(framelen) + " ms " + (" - exceeded 20 ms" if framelen>20 else "")

