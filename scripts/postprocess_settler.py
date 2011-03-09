
import Image, ImageDraw
import sys
import fnmatch
import os

def postproc_frames () : #filename, box) :

	imgnum = 0
	totalim = Image.new ("RGBA", (boundsize[0]*16, boundsize[1]*16))

	for i in range (firstframe, lastframe+1):

		print "... "+str(i)+"th frame"

		setim = Image.open (searchdir+"/noshd-"+str(i).zfill(3)+".png")
		for x in range(setim.size[0]) :
			for y in range(setim.size[1]) :
				pixel = list(setim.getpixel ((x,y)))
				if pixel[3] >= 128 :
					pixel[3] = 255
				else :
					pixel[3] = 0
				setim.putpixel ((x,y), tuple(pixel))

		shdim = Image.open (searchdir+"/onlshd-"+str(i).zfill(3)+".png")
		for x in range(shdim.size[0]) :
			for y in range(shdim.size[1]) :
				pixel = list(shdim.getpixel ((x,y)))
				if pixel[3] >= 64 :
					pixel[3] = 128
				else :
					pixel[3] = 0
				#pixel[0],pixel[1],pixel[2] +=
				shdim.putpixel ((x,y), tuple(pixel))
		
		shdim.paste (setim, None, setim)

		imgout = shdim.crop(tuple(bounds))
		totalim.paste (imgout, (boundsize[0]*(imgnum%16), boundsize[1]*(imgnum/16)))
		#imgout.save (outdir+"/"+str(i).zfill(3)+".png")
		imgnum+=1

	totalim.save (outname)

def find_bounds () :

	global bounds, boundsize

	pivotimg = Image.open (searchdir+"/noshd-001.png")
	bounds = list(pivotimg.size)+[0,0] # left, top, right, bottom

	for ff in os.listdir(searchdir):
		if fnmatch.fnmatch(ff, "*.png"):
			img = Image.open (searchdir+ff)
			imgbox = img.getbbox ()
			if imgbox[0] < bounds[0] :
				bounds[0] = imgbox[0]
			if imgbox[1] < bounds[1] :
				bounds[1] = imgbox[1]
			if imgbox[2] > bounds[2] :
				bounds[2] = imgbox[2]
			if imgbox[3] > bounds[3] :
				bounds[3] = imgbox[3]
	
	boundsize = [bounds[2]-bounds[0], bounds[3]-bounds[1]] # width, height

# ueberpruefe argumente
if len(sys.argv) != 5 :
	raise Exception("usage: script input-filedir output-filename firstframe lastframe")

searchdir, outname, firstframe, lastframe = sys.argv[1:]
firstframe = int(firstframe)
lastframe = int(lastframe)

print "finding bounds"
find_bounds ()

print "postprocess settler-frames"
postproc_frames ()

