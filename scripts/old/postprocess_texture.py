
import sys
import Image, ImageDraw

# ueberpruefe argumente
if len(sys.argv) != 3 :
	raise Exception("usage: script input-file output-file")

factor = 8		# vergroesserung des grund-dreiecks
gradwidth = 8	# breite der randverlaeufe

infilename = sys.argv[1]
outfilename = sys.argv[2]

texin = Image.open (infilename)
texin = texin.convert ("RGB")

# kopiere hinteres dreieck nach vorne
for y in range (factor*14) :
	for x in range (y) :
		texin.putpixel ((x, y), texin.getpixel ((x+factor*28, y)))

# schraeger verlaufs-streifen
for y in range (gradwidth) :
	for x in range (factor*28) :
		pix1 = list(texin.getpixel ((x, y)))
		pix2 = list(texin.getpixel ((factor*14+x, factor*14+y)))
		for i in range(len(pix1)) :
			pix1[i] = pix1[i] * float(y) / float(gradwidth) + pix2[i] * float(gradwidth-y) / float(gradwidth)
			pix1[i] = int(pix1[i])
		texin.putpixel ((x, y), tuple(pix1))

# oberer horizontaler verlaufs-streifen
for y in range (factor*14) :
	for x in range (gradwidth) :
		pix1 = list(texin.getpixel ((x+y, y)))
		pix2 = list(texin.getpixel ((factor*28+x+y, y)))
		for i in range(len(pix1)) :
			pix1[i] = pix1[i] * float(x) / float(gradwidth) + pix2[i] * float(gradwidth-x) / float(gradwidth)
			pix1[i] = int(pix1[i])
		texin.putpixel ((x+y, y), tuple(pix1))

# rechteck ausschneiden und speichern
texout = texin.crop((0, 0, 28*factor, 14*factor))
texout.save (outfilename)
