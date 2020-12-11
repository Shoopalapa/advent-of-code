<<<<<<< HEAD
import json

def main():
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()

		count = 0 
		group = set()
		for line in lines:
			if line != "":
				for character in line:
					group.add(character)
			else:
				count += len(group)
				group = set()
		count += len(group)
			

	print(count)

def step2():
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()

		count = 0 
		group = dict()
		groupCount = 0

		for line in lines:
			if line != "":
				groupCount += 1
				for character in line:
					if character not in group.keys():
						group[character] = 1
					else:
						group[character] += 1
			else:
				
				for key in group.keys():
					if group[key] == groupCount:
						count += 1
				# print(json.dumps(group,indent=1))
				# print(count)
				group = {}
				groupCount = 0
		
		for key in group.keys():
			if group[key] == groupCount:
				count += 1
		
			

	print(count)


=======
import json

def main():
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()

		count = 0 
		group = set()
		for line in lines:
			if line != "":
				for character in line:
					group.add(character)
			else:
				count += len(group)
				group = set()
		count += len(group)
			

	print(count)

def step2():
	with open('input.txt') as inputfile:
		lines = inputfile.read().splitlines()

		count = 0 
		group = dict()
		groupCount = 0

		for line in lines:
			if line != "":
				groupCount += 1
				for character in line:
					if character not in group.keys():
						group[character] = 1
					else:
						group[character] += 1
			else:
				
				for key in group.keys():
					if group[key] == groupCount:
						count += 1
				# print(json.dumps(group,indent=1))
				# print(count)
				group = {}
				groupCount = 0
		
		for key in group.keys():
			if group[key] == groupCount:
				count += 1
		
			

	print(count)


>>>>>>> 93e4f3d50c9370b0629b0c3b5cc1471c859e1289
step2()