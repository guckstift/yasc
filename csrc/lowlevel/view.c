
#include <stdio.h>
#include "SDL_opengl.h"

typedef unsigned int uint;

void GFXEngineSDLOGL_DrawTerrain (uint *mymap, uint mapsize, uint TRIA_W, uint TRIA_H,
	uint TEX_FACTOR, uint *textures);
void GFXEngineSDLOGL_DrawTriangle (uint tx, uint ty, uint upt,
	uint TRIA_W, uint TRIA_H, uint TEX_FACTOR, uint TEXTURE);


void GFXEngineSDLOGL_DrawTerrain (uint *mymap, uint mapsize, uint TRIA_W, uint TRIA_H,
	uint TEX_FACTOR, uint *textures)
{
	uint x,y;
	uint absx, absy;

	/* Draw Triangles */
	for (y=0; y<mapsize; y++) {
		for (x=0; x<mapsize; x++) {
			GFXEngineSDLOGL_DrawTriangle (x, y, (x+y)%2 == 1, TRIA_W, TRIA_H,
				TEX_FACTOR, textures[mymap[y*mapsize+x]]);
		}
	}
	/* Draw Borders */
}

void GFXEngineSDLOGL_DrawTriangle (uint tx, uint ty, uint upt,
	uint TRIA_W, uint TRIA_H, uint TEX_FACTOR, uint TEXTURE)
{
	float u;
	float v;
	uint x, y;
	
	x = tx*TRIA_W/2;
	y = ty*TRIA_H;

	u = (tx/(TEX_FACTOR*2.0)) + 0.5 * ( (ty%(TEX_FACTOR*2)) >= TEX_FACTOR );
	v = (ty/(float)(TEX_FACTOR));

	glBindTexture (GL_TEXTURE_2D, TEXTURE);
	glBegin (GL_TRIANGLES);
	if (!upt) {
		glTexCoord2f (u, v);
		glVertex3i (x, y, 0);
	
		glTexCoord2f (u+(1.0/TEX_FACTOR), v);
		glVertex3i (x+TRIA_W, y, 0);
	
		glTexCoord2f (u+(1.0/(TEX_FACTOR*2)), v+(1.0/TEX_FACTOR));
		glVertex3i (x+TRIA_W/2, y+TRIA_H, 0);
	}
	else {
		glTexCoord2f (u+(1.0/(TEX_FACTOR*2)), v);
		glVertex3i (x+TRIA_W/2, y, 0);
	
		glTexCoord2f (u+(1.0/TEX_FACTOR), v+(1.0/TEX_FACTOR));
		glVertex3i (x+TRIA_W, y+TRIA_H, 0);
	
		glTexCoord2f (u, v+(1.0/TEX_FACTOR));
		glVertex3i (x, y+TRIA_H, 0);
	}
	glEnd ();
}
