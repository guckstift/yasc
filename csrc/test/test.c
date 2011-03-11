
#include <stdio.h>

void give_matrix (int w, int h, int **vals)
{
	int x,y;
	
	for(y=0; y<h; y++) {
		for(x=0; x<w; x++) {
			printf ("%i ", vals[y][x]);
		}
		printf("\n");
	}
}
