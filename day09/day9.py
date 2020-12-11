def step1(lines, preamble):

	for i in range(preamble,len(lines)):
		tempList = lines[i-preamble:i]
		found = False
		
		for temp in tempList:
			lookingFor = int(lines[i]) - int(temp)
			if str(lookingFor) in tempList:
				found = True
		
		if not found:
			return(lines[i])

	return(-1,-1)

def step2(lines, preamble):
	brokenIndex, brokenNumber = -1,-1

	for i in range(preamble,len(lines)):
		tempList = lines[i-preamble:i]
		found = False
		
		for temp in tempList:
			lookingFor = int(lines[i]) - int(temp)
			if str(lookingFor) in tempList:
				found = True
		
		if not found:
			brokenIndex = int(i)
			brokenNumber = int(lines[i])

	for j in range(0,brokenIndex+1):
		testSum = 0
		testIndex = int(j)

		while testSum < brokenNumber:

			testSum += int(lines[testIndex])
			testIndex += 1

		if testSum == brokenNumber:
			sortedList = list(map(int,lines[j:(testIndex)]))
			sortedList.sort()
	
			return(int(sortedList[0]) + int(sortedList[-1]))

	return(-1,-1)

def main():
	inputfile = open('input.txt')
	lines = inputfile.read().splitlines()

	print(step1(lines,25))
	print(step2(lines,25))

main()
