import random

empty = "_"
filled = "X"
total_cost = 0


def make_maze(width, height):
	maze = [[empty for i in range(width)] for j in range(height)]
	for i in range(width):
		for j in range(height):
			toss = random.random() < 0.3
			if toss:
				maze[j][i] = filled
	maze[0][0] = "S"
	maze[height-1][width-1] = "T"
	return maze

def show_maze(maze):
	width, height = len(maze[0]), len(maze)
	for j in range(height):
		for i in range(width):
			print maze[j][i],
		print ""

def is_walkable(pt, maze):
	width, height = len(maze[0]), len(maze)
	x, y = pt
	if x < 0 or x >= width:
		return False
	if y < 0 or y >= height:
		return False
	return get_pt(maze, pt) in [empty, "S", "T"]

def get_pt(maze, pt):
	global total_cost
	total_cost += 1
	return maze[pt[1]][pt[0]]

# UR STUFF HERE
def neighborss(pt, maze): #get walkable neibour coordinate
	x, y = pt
	ret = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
	return filter(lambda x: is_walkable(x, maze), ret)

# given a point, return a list of points around it
def neighbors(pt, maze):
	x = pt[0]  
	y = pt[1] 
	max_x = len(maze[0])-1 #max_width
	max_y = len(maze)-1 #max_height
	if y < 1 : 
		n_up = "none" 
	else: 
		n_up = maze[y-1][x]
	if x+1 > max_x:
		n_right = "none"
	else:
		n_right = maze[y][x+1]
	if y+1 > max_y:
		n_down = "none"
	else: 
		n_down = maze[y+1][x]
	if x < 1:
		n_left = "none"
	else:
		n_left = maze[y][x-1]
	return (n_up,n_right,n_down,n_left) 

def walkable_neighbors(pt, maze):
	if any(direction == "_" or direction == "T" for direction in neighbors(pt, maze)):
		return True
	else:
		return False

def is_solvable(maze, pt):
	def _is_solvable(maze,pt,ctr):
		width, height = len(maze[0]), len(maze)
		if ctr > 10:
			return False
		if get_pt(maze, pt) == "T":
			return True
		s = [_is_solvable(maze, i, ctr+1) for i in neighborss(pt,maze)]
		return True in s
	return _is_solvable(maze, pt, 0)

def is_solvable_pu(maze, pt):
	def _is_solvable_pu(maze,pt,seen_pt):
		if pt in seen_pt:
			return False
		if get_pt(maze, pt) == "T":
			return True
		else:
			neighbors = neighborss(pt, maze)
			rest_sol = [_is_solvable_pu(maze, nn, seen_pt + [pt]) for nn in neighbors]
			return True in rest_sol
	return _is_solvable_pu(maze, pt, [])

def is_solvable_fringe(maze, pt):
	def _is_solvable_fringe(maze, fringe_pts, seen_pts):
		fringe_values = [get_pt(maze, ptt) for ptt in fringe_pts]
		if "T" in fringe_values:
			return True
		if fringe_pts == []:
			return False
		seen_pts = seen_pts + fringe_pts
		# expand the fringe
		next_fringe = [neighborss(fringe_pt, maze) for fringe_pt in fringe_pts]
		nxt_fringe_filtered = []
		for nxt_fr in next_fringe:
			nxt_fringe_filtered += filter(lambda x: x not in seen_pts, nxt_fr)
		return _is_solvable_fringe(maze, nxt_fringe_filtered, seen_pts)
	return _is_solvable_fringe(maze, [(0,0)], [(0,0)])

