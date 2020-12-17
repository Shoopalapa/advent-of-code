import pprint

def step1(lines):
	ranges = []
	for line in lines[0].split("\n"):
		options = line.split(": ")[1]
		optionsParsed = options.split(" or ")
		
		for option in optionsParsed:
			rangeParsed = option.split("-")
			ranges.extend(list(range(int(rangeParsed[0]),int(rangeParsed[1])+1)))

	total = 0
	ughList = []
	for line in lines[2].split("\n")[1:]:
		flag = False
		for num in line.split(","):
			numInt = int(num)
			if numInt not in ranges:
				total += numInt
				flag = True
		if not flag:
			ughList.append(line)

	# print(len(lines[2].split("\n")[1:]),len(ughList))
	return(total,ughList)

def step2(lines,ughList):
	fieldDict = {}
	for line in lines[0].split("\n"):
		field = line.split(":")[0]
		fieldDict[field] = (list(range(20)),[])

		options = line.split(": ")[1]
		optionsParsed = options.split(" or ")
		
		for option in optionsParsed:
			rangeParsed = option.split("-")
			fieldDict[field][1].extend(list(range(int(rangeParsed[0]),int(rangeParsed[1])+1)))
	
	# print(fieldDict["departure location"][0])
	# print(fieldDict["departure station"][0])
	# print(fieldDict["departure platform"][0])

	# print(fieldDict["departure platform"][0])

	# print(fieldDict["departure platform"][0])

	# print(fieldDict["departure platform"][0])

	for line in ughList:
		lineSplit = line.split(",")
		for i in range(len(lineSplit)):
			for j in fieldDict.keys():
				if i in fieldDict[j][0] and int(lineSplit[i]) not in fieldDict[j][1]:
					# print("Removing " + str(i) + " from " + j + ". " + lineSplit[i])
					fieldDict[j][0].remove(i)

	# print(fieldDict["departure location"][0])
	# print(fieldDict["departure station"][0])
	# print(fieldDict["departure platform"][0])
	# print(fieldDict["departure track"][0])
	# print(fieldDict["departure date"][0]
	# print(fieldDict["departure time"][0])
	hatemylife = [0] * 20
	for item in fieldDict.keys():
		print(item, fieldDict[item][0])
		for num in fieldDict[item][0]:
			hatemylife[num] += 1

	gah = [""] * 20
	print(hatemylife)


	while hatemylife.count(1) != 0:
		index = hatemylife.index(1)
		for item, value in fieldDict.items():
			if index in value[0]:
				gah[index] = item

				for plop in value[0]:
					for pip,pop in fieldDict.items():
						if plop in pop[0]:
							pop[0].remove(plop)
					hatemylife[plop] -= 1
	print(gah)
	print("hi")
	return() 

def main():
	with open("input.txt") as inputfile:
		lines = inputfile.read().split("\n\n")
		result,ughList = step1(lines)
		print(result)
		pprint.pprint(step2(lines,ughList))


main()
