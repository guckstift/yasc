#!/usr/bin/env python
# -*- coding: utf-8 -*-


def path_heuristic(sx, sy, ex, ey):
	"""
	Calculates the distance of the shortest path between start- (sx,sy) and endpoint (ex,ey).
	@param sx the x-coordinate of the startpoint
	@param sy the y-coordinate of the startpoint
	@param ex the x-coordinate of the endpoint
	@param ey the y-coordinate of the endpoint
	@return the minimal distance between the start- and endpoint
	"""
	
	dx = abs(sx - ex)	# delta x - the distance in x-direction
	dy = abs(sy - ey)	# delta y - the distance in y-direction
	
	man_dist = dx + dy	# the manhattan-distance between start- and endpoint
	
	if sx == ex or sy == ey:
		return man_dist		# there are no diagonals at the shortes path
	
	diagonal = (sx > ex and sy < ey ) or (sx < ex and sy > ey) # True if there is one (or more) diagonal like this: /. False if \
	vert_dir = (sy > ey)	# vertical direction, True if endpoint is above the startpoint, False otherwise
	line_par = sy%2 == 1	# True if lineindex is odd 1, False otherwise
	
	if diagonal ^ vert_dir ^ line_par:
		max_diagonals = int((dy+1)/2)
	else:
		max_diagonals = int(dy/2)
	
	# max_diagonals is the maximum number of diagonals along the path from start to end
	
	return man_dist - min(dx, max_diagonals)

# some tests:
print path_heuristic (0,0, 0,3) == 3 # rechts runter
print path_heuristic (3,0, 0,3) == 4 # links runter
print path_heuristic (3,0, 3,0) == 0 # stehen bleiben
print path_heuristic (1,5, 4,1) == 5 # rechts hoch
print path_heuristic (3,5, 0,0) == 6 # links hoch
