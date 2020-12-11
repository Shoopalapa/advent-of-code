<<<<<<< HEAD
import re
import json 

def main(ogBag):
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()
		bagDict = {}

		for rule in lines:
			ruleParsed = rule.split(" contain ")
			
			mainItem = ruleParsed[0]
			subItems = [x.strip() for x in re.split("[,.]",ruleParsed[1]) ][:-1]

			bagDict[mainItem] = subItems

		containingBags = [ogBag]
		counter = 0

		while counter < len(containingBags):
			for key in bagDict.keys():
				for item in bagDict[key]:
					if containingBags[counter][:-1] in item and key not in containingBags:
						containingBags.append(key)
			counter += 1


		print(len(containingBags) -1 )

def improvement(ogBag):
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()
		bagDict = {}

		for rule in lines:
			ruleParsed = rule.split(" contain ")
			
			mainItem = ruleParsed[0].replace(" bags","")
			subItems = [x.strip() for x in re.split("[,.]",ruleParsed[1]) ][:-1]
			subItemsParsed = []
			for subItem in subItems:
				blah = subItem.split(" ")
				subItemsParsed.append((blah[0]," ".join(blah[1:-1])))\

			bagDict[mainItem] = subItemsParsed
		print(improvementHelper(ogBag,bagDict)-1)

def improvementHelper(bag, bags):
	if bags[bag]:
		count = 0
		for testBag in bags[bag]:
			if testBag[1] not in "other":
				count += 1 + (int(testBag[0]) * int(improvementHelper(testBag[1],bags)))
		return count
	else:
		return 1
		
main('shiny gold bag')
improvement('shiny gold')
=======
import re
import json 

def main(ogBag):
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()
		bagDict = {}

		for rule in lines:
			ruleParsed = rule.split(" contain ")
			
			mainItem = ruleParsed[0]
			subItems = [x.strip() for x in re.split("[,.]",ruleParsed[1]) ][:-1]

			bagDict[mainItem] = subItems

		containingBags = [ogBag]
		counter = 0

		while counter < len(containingBags):
			for key in bagDict.keys():
				for item in bagDict[key]:
					if containingBags[counter][:-1] in item and key not in containingBags:
						containingBags.append(key)
			counter += 1


		print(len(containingBags) -1 )

def improvement(ogBag):
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()
		bagDict = {}

		for rule in lines:
			ruleParsed = rule.split(" contain ")
			
			mainItem = ruleParsed[0].replace(" bags","")
			subItems = [x.strip() for x in re.split("[,.]",ruleParsed[1]) ][:-1]
			subItemsParsed = []
			for subItem in subItems:
				blah = subItem.split(" ")
				subItemsParsed.append((blah[0]," ".join(blah[1:-1])))\

			bagDict[mainItem] = subItemsParsed
		print(improvementHelper(ogBag,bagDict)-1)

def improvementHelper(bag, bags):
	if bags[bag]:
		count = 0
		for testBag in bags[bag]:
			if testBag[1] not in "other":
				count += 1 + (int(testBag[0]) * int(improvementHelper(testBag[1],bags)))
		return count
	else:
		return 1
		
main('shiny gold bag')
improvement('shiny gold')
>>>>>>> 93e4f3d50c9370b0629b0c3b5cc1471c859e1289
