import time
import pprint

def part1(lines):
	estimate = int(lines[0])
	busTimes = lines[1].split(",")
	
	while "x" in busTimes:
		busTimes.remove("x")
	busTimes = list(map(int,busTimes))

	earliestBus,earliestTime = -1, -1
	for contender in busTimes:
		offSet = estimate % contender
		contenderEarliest = contender - offSet

		if contenderEarliest < earliestTime or earliestTime < 0:
			earliestTime, earliestBus = contenderEarliest, contender

	return(earliestTime*earliestBus)

def part2(lines):
	start_time = time.time()
	estimatedTimes = []
	busTimes = lines[1].split(",")
	winner = False

	myDict = {}
	myDict2 = {}
	for index in range(len(busTimes)):
		if (busTimes[index] != "x"):
			myDict[index] = int(busTimes[index])
			myDict2[busTimes[index]] = index


	pprint.pprint(myDict,width=1)
	pprint.pprint(myDict2,width=1)

	myMax = max(myDict.values())
	myIndex = myDict2[str(myMax)]

	i = 1000000 * myMax
	while not winner:
		count = 0
		for contender in (myDict.keys()):
			if (i + (int(contender) - myIndex))%myDict[contender] == 0:
				count += 1
		if count == len(myDict.keys()):
			winner = True

		i += myMax
	# while not winner:
	# 	count = 0
	# 	for j in range(len(busTimes)):
	# 		if busTimes[j] == "x" or (i+j)%int(busTimes[j]) == 0:
	# 			count +=1
	# 	if count == len(busTimes):
	# 		winner = True
	# 	i += 1
		
		# if i >= 1000000 and (i%1000000==0):
		# 	print()
		# 	elapsedTime = time.time() - start_time
		# 	timePer = elapsedTime / (i/1000000)
		# 	estimatedTime = timePer * (100000000000000//1000000)
		# 	estimatedTimes.append(estimatedTime)
		# 	print("Likely " + str(sum(estimatedTimes)/len(estimatedTimes)) + " until done...")

	return(i-myMax-myIndex)

def main():
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()
		#print(part1(lines))
		print(part2(lines))
main()
