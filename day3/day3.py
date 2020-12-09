def main(right,down):
	with open("input.txt","r") as inputfile:
		myMap = inputfile.read()
		ridges = myMap.splitlines()

		treeCount = 0
		globalIndex = 0
		localIndex = 0

		for ridge in ridges[1:]:
			globalIndex += right
			localIndex = globalIndex % len(ridge)
			if(ridge[localIndex] == "#"):
				treeCount += 1

		print("You hit " + str(treeCount) +" trees!")
		return treeCount


def improvement(right,down):
	with open("input.txt","r") as inputfile:
		myMap = inputfile.read()
		ridges = myMap.splitlines()

		treeCount = 0
		globalIndex = 0
		localIndex = 0

		# for ridge in ridges[1:]:
		for ridgeIndex, ridge in enumerate(ridges[down:]):
			if(ridgeIndex % down == 0):
				globalIndex += right
				localIndex = globalIndex % len(ridge)
				if(ridge[localIndex] == "#"):
					treeCount += 1

		print("You hit " + str(treeCount) +" trees!")
		return treeCount

print(str(improvement(1,1)*improvement(3,1)*improvement(5,1)*improvement(7,1)*improvement(1,2)) + " trees total. Oof.")
