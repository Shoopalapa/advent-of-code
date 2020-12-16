def bothsteps(lines,steps):
	startingInput = lines.split(",")

	numDict = {}
	for index in range(len(startingInput)):
		numDict[int(startingInput[index])] = [index+1]		
	
	currentNum = 6
	#I know these nested statements are gross, but they work and I want to relax by my fire :)
	for i in range(len(startingInput)+1,steps+1):
		if currentNum in numDict.keys():
			if len(numDict[currentNum]) >= 2:
				currentNum =  numDict[currentNum][-1] - numDict[currentNum][-2]
				if currentNum in numDict.keys():
					numDict[currentNum].append(i)
				else:
					numDict[currentNum] = [i]
			else:
				currentNum = 0
				numDict[0].append(i)
		else:
			currentNum = 0
			numDict[0].append(i)



	print(currentNum)
	print(numDict)

def main():
	testinput = "0,3,6"
	realinput = "19,0,5,1,10,13"
	print(bothsteps(realinput,30000000))

main()