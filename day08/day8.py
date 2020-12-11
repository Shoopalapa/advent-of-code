<<<<<<< HEAD
def step1(instructions):
	completedInstructions = []
	step = 0
	myGlobal = 0

	while step not in completedInstructions:
		
		command = instructions[step][:3]
		number = instructions[step][4:]

		if "acc" in command:
			myGlobal += int(number)
			completedInstructions.append(step)
			step += 1
		elif command == "jmp":
			completedInstructions.append(step)
			step += int(number)
		else:
			completedInstructions.append(step)
			step +=1

	return ("Total is " + str(myGlobal))

def step2(instructions):


	for i in range(len(instructions)):
		
		tempInstructions = list(instructions)

		if "jmp" in tempInstructions[i]:
			tempInstructions[i] = "nop " + tempInstructions[i][4:]
		elif "nop" in tempInstructions[i]:
			tempInstructions[i] = "jmp " + tempInstructions[i][4:]
		
		result = runHelper(tempInstructions,i) 
		
		if result > 0:
			return("Step " + str(i) + " with result " + str(result))
		


def runHelper(instructions,step):
	completedInstructions = []
	myGlobal = 0
	localStep = 0

	while localStep not in completedInstructions:
		if localStep == len(instructions):
			return myGlobal

		command = instructions[localStep][:3]
		number = instructions[localStep][4:]

		if "acc" in command:
			myGlobal += int(number)
			completedInstructions.append(localStep)
			localStep += 1
		elif command == "jmp":
			completedInstructions.append(localStep)
			localStep += int(number)
		else:
			completedInstructions.append(localStep)
			localStep +=1

	return -1

def main():
	with open("input.txt") as inputfile:
		instructions = inputfile.read().splitlines()

		print(step1(instructions))
		print(step2(instructions))

main()
=======
def step1(instructions):
	completedInstructions = []
	step = 0
	myGlobal = 0

	while step not in completedInstructions:
		
		command = instructions[step][:3]
		number = instructions[step][4:]

		if "acc" in command:
			myGlobal += int(number)
			completedInstructions.append(step)
			step += 1
		elif command == "jmp":
			completedInstructions.append(step)
			step += int(number)
		else:
			completedInstructions.append(step)
			step +=1

	return ("Total is " + str(myGlobal))

def step2(instructions):


	for i in range(len(instructions)):
		
		tempInstructions = list(instructions)

		if "jmp" in tempInstructions[i]:
			tempInstructions[i] = "nop " + tempInstructions[i][4:]
		elif "nop" in tempInstructions[i]:
			tempInstructions[i] = "jmp " + tempInstructions[i][4:]
		
		result = runHelper(tempInstructions,i) 
		
		if result > 0:
			return("Step " + str(i) + " with result " + str(result))
		


def runHelper(instructions,step):
	completedInstructions = []
	myGlobal = 0
	localStep = 0

	while localStep not in completedInstructions:
		if localStep == len(instructions):
			return myGlobal

		command = instructions[localStep][:3]
		number = instructions[localStep][4:]

		if "acc" in command:
			myGlobal += int(number)
			completedInstructions.append(localStep)
			localStep += 1
		elif command == "jmp":
			completedInstructions.append(localStep)
			localStep += int(number)
		else:
			completedInstructions.append(localStep)
			localStep +=1

	return -1

def main():
	with open("input.txt") as inputfile:
		instructions = inputfile.read().splitlines()

		print(step1(instructions))
		print(step2(instructions))

main()
>>>>>>> 93e4f3d50c9370b0629b0c3b5cc1471c859e1289
