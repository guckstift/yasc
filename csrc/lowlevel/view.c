
#include <stdio.h>
#include "SDL_opengl.h"

typedef unsigned int uint;

void GFXEngineSDLOGL_DrawTerrain (uint **terra, uint mapsize, uint TRIA_W, uint TRIA_H,
	uint TEX_FACTOR, uint *textures, int ***vertmap);

void GFXEngineSDLOGL_DrawTerrain (uint **terra, uint mapsize, uint TRIA_W, uint TRIA_H,
	uint TEX_FACTOR, uint *textures, int ***vertmap)
{
	uint x,y;
	uint absx, absy;
	int *vert;
	float u;
	float v;
	uint upt;
	
	/* Draw Triangles */
	for (y=0; y<mapsize; y++) {
		for (x=0; x<mapsize; x++) {
		
			upt = (x+y)%2 == 1;
			u = (x/(TEX_FACTOR*2.0)) + 0.5 * ( (y%(TEX_FACTOR*2)) >= TEX_FACTOR );
			v = (y/(float)(TEX_FACTOR));

			glBindTexture (GL_TEXTURE_2D, textures[terra[y][x]]);
			
			/* Line-loop to demonstrate the height map is working */
			glBegin (GL_LINE_LOOP);
			/*glBegin (GL_TRIANGLES);*/
			
			if (!upt) {
				glTexCoord2f (u, v);
				vert = vertmap[y][x/2];
				glVertex3i (vert[0], vert[1], 0);
	
				glTexCoord2f (u+(1.0/TEX_FACTOR), v);
				vert = vertmap[y][x/2+1];
				glVertex3i (vert[0], vert[1], 0);
	
				glTexCoord2f (u+(1.0/(TEX_FACTOR*2)), v+(1.0/TEX_FACTOR));
				vert = vertmap[y+1][x/2+(y%2)];
				glVertex3i (vert[0], vert[1], 0);
			}
			else {
				glTexCoord2f (u+(1.0/(TEX_FACTOR*2)), v);
				vert = vertmap[y][(x+1-(y%2))/2];
				glVertex3i (vert[0], vert[1], 0);
	
				glTexCoord2f (u+(1.0/TEX_FACTOR), v+(1.0/TEX_FACTOR));
				vert = vertmap[y+1][1+(x-1+(y%2))/2];
				glVertex3i (vert[0], vert[1], 0);
	
				glTexCoord2f (u, v+(1.0/TEX_FACTOR));
				vert = vertmap[y+1][(x-1+(y%2))/2];
				glVertex3i (vert[0], vert[1], 0);
			}
			glEnd ();
		}
	}
	/* Draw Borders */
	/* to be implemented */
}

