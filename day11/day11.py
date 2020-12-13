from pprint import pprint
from copy import deepcopy

def step1(grid):
	rows = len(grid)
	columns = len(grid[0]) 

	newGrid = list()
	for blah in range(len(grid)):
		grid[blah] = [seat for seat in grid[blah]]
		newGrid.append([seat for seat in grid[blah]])

	changed = True
	while changed:
		changed = False
		for i in range(rows):
			for j in range(columns):
				count = 0 

				for x in range(max(0,j-1), min(j+1,columns-1)+1):
					for y in range(max(0,i-1), min(i+1,rows-1)+1):
						if grid[y][x] == "#" and (x,y) != (j,i):
							
							count += 1

			
				if grid[i][j] == "L" and count == 0:
					newGrid[i][j] = "#"
					changed = True

				elif grid[i][j] == "#" and count >= 4:
					newGrid[i][j] = "L"
					changed = True

		grid = [plop[:] for plop in newGrid]

	bobcount = 0 
	for bob in grid:
		for pah in bob:
			if pah == "#":
				bobcount += 1
	return(bobcount)

def step2(grid):
	rows = len(grid)
	columns = len(grid[0]) 

	newGrid = list()
	for blah in range(len(grid)):
		grid[blah] = [seat for seat in grid[blah]]
		newGrid.append([seat for seat in grid[blah]])

	changed = True
	neighborDict = {"n":"","e":"","s":"","w":"","ne":"","se":"","sw":"","nw":""}
	while changed:
		changed = False
		for i in range(rows):
			for j in range(columns):
				count = 0 
				ring = 1

				while not all(neighbor != "" for neighbor in neighborDict.values()):
					#pprint(neighborDict,width=1)

					if neighborDict["w"] == "":
						if j == 0:
							neighborDict["w"] = "."
						elif j-ring == 0:
							neighborDict["w"] = grid[i][j-ring]
						elif grid[i][j-ring] != ".":
							neighborDict["w"] = grid[i][j-ring]
				 	
					if neighborDict["n"] == "":
						if i == 0:
							neighborDict["n"] = "."
						elif i-ring == 0:
							neighborDict["n"] = grid[i-ring][j]
						elif grid[i-ring][j] != ".":
							neighborDict["n"] = grid[i-ring][j]

					if neighborDict["s"] == "":
						if i == rows - 1:
							neighborDict["s"] = "."
						elif i+ring == rows - 1:
							neighborDict["s"] = grid[i+ring][j]
						elif grid[i+ring][j] != ".":
							neighborDict["s"] = grid[i+ring][j]

					if neighborDict["e"] == "":
						if j == columns - 1:
							neighborDict["e"] = "."
						elif j+ring == columns - 1:
							neighborDict["e"] = grid[i][j+ring]
						elif grid[i][j+ring] != ".":
							neighborDict["e"] = grid[i][j+ring]

					if neighborDict["nw"] == "":
						if j == 0 or i == 0:
							neighborDict["nw"] = "."
						elif j-ring == 0 or i-ring ==0:
							neighborDict["nw"] = grid[i-ring][j-ring]
						elif grid[i-ring][j-ring] != ".":
							neighborDict["nw"] = grid[i-ring][j-ring]

					if neighborDict["se"] == "":
						if j == columns - 1 or i == rows - 1:
							neighborDict["se"] = "."
						elif j+ring == columns - 1 or i+ring == rows - 1:
							neighborDict["se"] = grid[i+ring][j+ring]
						elif grid[i+ring][j+ring] != ".":
							neighborDict["se"] = grid[i+ring][j+ring]

					if neighborDict["ne"] == "":
						if j == columns - 1 or i == 0:
							neighborDict["ne"] = "."
						elif j+ring == columns - 1 or i-ring == 0:
							neighborDict["ne"] = grid[i-ring][j+ring]
						elif grid[i-ring][j+ring] != ".":
							neighborDict["ne"] = grid[i-ring][j+ring]

					if neighborDict["sw"] == "":
						if j == 0 or i == rows - 1:
							neighborDict["sw"] = "."
						elif j-ring == 0 or i+ring == rows - 1:
							neighborDict["sw"] = grid[i+ring][j-ring]
						elif grid[i+ring][j-ring] != ".":
							neighborDict["sw"] = grid[i+ring][j-ring]
					ring += 1

				count = sum(value == "#" for value in neighborDict.values())
				if grid[i][j] == "L" and count == 0:
					newGrid[i][j] = "#"
					changed = True

				elif grid[i][j] == "#" and count >= 5:
					newGrid[i][j] = "L"
					changed = True

				neighborDict = {"n":"","e":"","s":"","w":"","ne":"","se":"","sw":"","nw":""}

		grid = [plop[:] for plop in newGrid]

	bobcount = 0 
	for bob in grid:
		for pah in bob:
			if pah == "#":
				bobcount += 1
	return(bobcount)

def main():
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()
		print(step1(lines))
		print(step2(lines))

main()