# Find number of passwords that contain the specified character within a range
def main1():

	with open("input.txt","r") as inputfile:
		reader = inputfile.read()
		lines = reader.splitlines()

		eligiblePWs = 0
		for line in lines:
			parsedPW = line.split()

			count = parsedPW[0].split("-")
			character = parsedPW[1][0]
			password = parsedPW[2]

			countMin = int(count[0])
			countMax = int(count[-1])

			result = password.count(character)
			if  (result >= countMin) & (result <= countMax ):
				eligiblePWs += 1
		print(str(eligiblePWs) + " passwords are eligible!")

# Find number of password that contain a specified character at exclusively one of the locations
def main2():

	with open("input.txt","r") as inputfile:
		reader = inputfile.read()
		lines = reader.splitlines()

		eligiblePWs = 0
		for line in lines:
			parsedPW = line.split()

			count = parsedPW[0].split("-")
			character = parsedPW[1][0]
			password = parsedPW[2]

			countMin = int(count[0])
			countMax = int(count[-1])

			if (password[countMin-1] == character) != (password[countMax-1] == character):
				eligiblePWs += 1
		print(str(eligiblePWs) + " passwords are eligible!")


main2()