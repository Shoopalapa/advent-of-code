import math
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

	busTimes = lines[1].split(",")

	crtDict = {}
	for index in range(len(busTimes)):
		if (busTimes[index] != "x"):
			crtDict[-index] = {"mod": int(busTimes[index]), "Ni": "", "Xi": ""}

	# print(type(crtDict[1]["mod"]))

	N = 1
	for busTime in crtDict.keys():
		N *= crtDict[busTime]["mod"]

	for busTime in crtDict.keys():
		crtDict[busTime]["Ni"] = N//crtDict[busTime]["mod"]

	for busTime in crtDict.keys():
		crtDict[busTime]["Xi"] = solveMod(crtDict[busTime]["Ni"],1,crtDict[busTime]["mod"])


	ultimaMod = 0
	for busTime in crtDict.keys():
		ultimaMod += (math.prod(crtDict[busTime].values()) * busTime)//crtDict[busTime]["mod"]


	return(ultimaMod%N)

def solveMod(multiplier,remainder,mod):

	for i in range(10*mod):
		if (multiplier*i)%mod==remainder:
			return(i)

def main():
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()
		#print(part1(lines))
		print(part2(lines))

main()