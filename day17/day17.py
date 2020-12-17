import copy 
import pprint

def step1(lines,steps):
	space = ([["."*len(lines[0])] * len(lines)] * steps) + [lines] + ([["."*len(lines[0])]*len(lines)]*steps)
	currentSpace = copy.deepcopy(space)

	for itr in range(steps):
		pass
	return(space)

def returnNeighbors(x,y,z,boundaryXY,boundaryZ,distance=1,):
	neighbors = []
	for a in range(-distance,distance+1):
		for b in range(-distance,distance+1):
			for c in range(-distance,distance+1):
				diffX = x+a
				diffY = y+b
				diffZ = z+c
				if not (diffX<0 or diffY<0 or diffZ<0 or diffX>boundaryXY or diffY>boundaryXY or diffZ>boundaryZ or a,b,c==0,0,0):
					neighbors.append((x+a,y+b,z+c))

	return(neighbors)

def step2(lines):
	pass

def main():
	with open("inputtest.txt") as inputfile:
		lines = inputfile.read().splitlines()
		pprint.pprint(step1(lines,1))

#main()
print(returnNeighbors(7,7,7,9,6,1))