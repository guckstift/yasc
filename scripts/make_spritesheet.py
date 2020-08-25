#!/usr/bin/env python3

from sys import argv
from PIL import Image
from os import listdir

outputsize = 1024,1024
midpoint = 256,406

if len(argv) < 2:
	exit("no input dir passed")

inputdir = argv[1]
itemlist = listdir(inputdir)
paths = list(map(lambda filename: inputdir + "/" + filename, itemlist))
images = list(map(lambda path: Image.open(path), paths))
inputwidth, inputheight = images[0].size

left = inputwidth
right = 0
top = inputheight;
bottom = 0

for im in images:
	for y in range(inputheight):
		for x in range(inputwidth):
			pixel = im.getpixel((x,y))
			
			if pixel[3] > 0:
				left = min(left, x)
				top = min(top, y)
				right = max(right, x + 1)
				bottom = max(bottom, y + 1)

framew = right - left
frameh = bottom - top

print("l", left, "t", top, "w", framew, "h", frameh)

outim = Image.new("RGBA", outputsize, 0)
xframes = outputsize[0] // framew
yframes = outputsize[1] // frameh
curx = 0
cury = 0

print(xframes, yframes)

for im in images:
	cropped = im.crop((left, top, right, bottom))
	outim.paste(cropped, (curx, cury))
	curx += framew
	
	if curx >= outputsize[0] - framew:
		curx = 0
		cury += frameh

outim.save("test.png")
