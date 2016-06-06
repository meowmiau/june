execfile("maze.py")

print "our maze"
maze1 = make_maze(5,5)
show_maze(maze1)

print "raw format"
print maze1

print "is 3, 1 walkable?"
print is_walkable((3,1), maze1)

print "is walkable?"
print neighborss((4,3), maze1)

print "can be solved?"


print neighborss((0,0),maze1)

print is_solvable(maze1,(0,0))

print "total_cost ", total_cost

def measure_cost(mazes, solver):
	global total_cost
	total_cost = 0
	for maze in mazes:
		res = solver(maze, (0,0))
	return float(total_cost) / len(mazes)

mazes = [make_maze(5,5) for i in range(10)]
print "measuring cost on two solvers"

print measure_cost(mazes, is_solvable)
print measure_cost(mazes, is_solvable_pu)
print measure_cost(mazes, is_solvable_fringe)

