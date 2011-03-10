


def path_heuristic(sx, sy, ex, ey):
	dx = abs(sx - ex)	# delta x
	dy = abs(sy - ey)	# delta y
	
	man_dist = dx + dy	# the manhattan-distance between start- and endpoint
	
	"""
	if (sx < ex and sy < ey ) or (sx > ex and sy > ey):
		diagonal = False	# there is one (or more) diagonal like this: \
	if (sx > ex and sy < ey ) or (sx < ex and sy > ey):
		diagonal = True	# there is one (or more) diagonal like this: /
	"""
	if sx == ex or sy == ey:
		return man_dist	# there are no diagonal at the shortes path
	
	diagonal = (sx > ex and sy < ey ) or (sx < ex and sy > ey) # True if there is one (or more) diagonal like this: /
	vert_dir = (sy > ey)	# vertical direction (endpoint is above the startpoint)
	line_par = sy%2 == 1	# true if the lineparity is 1, false otherwise
	
	if diagonal ^ vert_dir ^ line_par:
		max_diagonals = int((dy+1)/2)
	else:
		max_diagonals = int(dy/2)
	
	return man_dist - min(dx, max_diagonals)

print path_heuristic (0,0, 0,3) == 3 # rechts runter
print path_heuristic (3,0, 0,3) == 4 # links runter
print path_heuristic (3,0, 3,0) == 0 # stehen bleiben
print path_heuristic (1,5, 4,1) == 5 # rechts hoch
print path_heuristic (3,5, 0,0) == 6 # links hoch
