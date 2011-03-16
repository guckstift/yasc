#!/usr/bin/env python
# -*- coding: utf-8 -*-


def path_heuristic(start, end):
	"""
	Calculates the distance of the shortest path between start- (sx,sy) and endpoint (ex,ey).
	@param start a coordinat-tuple (x,y) of the startpoint
	@param end a coordinat-tuple (x,y) of the endpoint
	@return the minimal distance between the start- and endpoint
	"""
	sx = start[0] 	# the x-coordinate of the startpoint
	sy = start[1]	# the y-coordinate of the startpoint
	ex = end[0]	# the x-coordinate of the endpoint
	ey = end[1]	# the y-coordinate of the endpoint
	
	dx = abs(sx - ex)	# delta x - the distance in x-direction
	dy = abs(sy - ey)	# delta y - the distance in y-direction
	
	man_dist = dx + dy	# the manhattan-distance between start- and endpoint
	
	if sx == ex or sy == ey:
		return man_dist		# there are no diagonals at the shortes path
	
	diagonal = (sx > ex and sy < ey ) or (sx < ex and sy > ey) # True if there is one (or more) diagonal like this: /. False if \
	vert_dir = (sy > ey)	# vertical direction, True if endpoint is above the startpoint, False otherwise
	line_par = sy%2 == 1	# True if lineindex is odd, False otherwise
	
	if diagonal ^ vert_dir ^ line_par:
		max_diagonals = int((dy+1)/2)
	else:
		max_diagonals = int(dy/2)
	
	# max_diagonals is the maximum number of diagonals along the path from start to end
	
	return man_dist - min(dx, max_diagonals)
