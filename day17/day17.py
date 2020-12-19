import copy 
import pprint

def step1(lines,steps):
	space = ([[["."]*len(lines[0])] * len(lines)] * steps) + [lines] + ([[["."]*len(lines[0])]*len(lines)]*steps)
	currentSpace = copy.deepcopy(space)

	pprint.pprint(space[0])
	# for itr in range(steps):
	# 	print("Cycle #"+str(itr+1))

	# 	for z in range(steps+1):
	# 		print("Z="+str(z))

	# 		for y in range(len(lines)):
	# 			for x in range(len(lines[0])):

	# 				count = 0
	# 				for neighbor in returnNeighbors(x,y,z,len(lines)-1,steps,1):
	# 					if currentSpace[neighbor[0]][neighbor[1]][neighbor[2]] == "#":
	# 						count += 1

	# 				if space[x][y][z] == "#" and not(count == 2 or count == 3):
	# 					currentSpace[x][y][z] = "."
	# 				elif space[x][y][z] == "." and count == 3:
	# 					currentSpace[x][y][z] == "#"
	# 				else:
	# 					currentSpace[x][y][z] == space[x][y][z]

	# 		pprint.pprint(currentSpace[x][y])
	# 	space = copy.deepcopy(currentSpace)

	return(space)

def returnNeighbors(x,y,z,boundaryXY,boundaryZ,distance=1,):
	neighbors = []
	for a in range(-distance,distance+1):
		for b in range(-distance,distance+1):
			for c in range(-distance,distance+1):
				diffX = x+a
				diffY = y+b
				diffZ = z+c
				if not (diffX<0 or diffY<0 or diffZ<0 or diffX>boundaryXY or diffY>boundaryXY or diffZ>boundaryZ):
					neighbors.append((x+a,y+b,z+c))

	return(neighbors)

def step2(lines):
	pass

def main():
	with open("inputtest.txt") as inputfile:
		lines = inputfile.read().splitlines()
		pprint.pprint(step1(lines,1))

main()
#print(returnNeighbors(0,0,6,9,6,1))