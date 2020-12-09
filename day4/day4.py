import json
import re

def main():

	with open("input.txt") as inputfile:
		passportFile = inputfile.read()
		rawPassports = passportFile.splitlines()

		scrubbedPassports = []
		currentPassport = {}

		requiredKeys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
		optionalKeys = {"cid"}

		validPassports = 0 

		for entry in rawPassports:
			if entry != '':
				scrubbedEntry = entry.split(" ")
				for keyValue in scrubbedEntry:
					key = keyValue.split(":")[0]
					value = keyValue.split(":")[1]
					currentPassport[key] = value
			else:
				scrubbedPassports.append(currentPassport)
				currentPassport = {}

		scrubbedPassports.append(currentPassport)


		validPassports = 0 
		for entry in scrubbedPassports:
			if (entry.keys() >= requiredKeys) and validation(entry):
				validPassports += 1 

		print(validPassports)
		#print(json.dumps(scrubbedPassports, indent=1))


def validation(entry):
	
	try:
		byr = int(entry['byr'])
		iyr = int(entry['iyr'])
		eyr = int(entry['eyr'])
		
		hgtVal = int(entry['hgt'][:-2])
		hgtTyp = entry['hgt'][-2:]
		hcl = entry['hcl']
		ecl = entry['ecl']
		pid = int(entry['pid'])

		ExpirationResult = byr in range(1920,2002+1) and iyr in range(2010,2020+1) and eyr in range(2020,2030+1)

		if hgtTyp == "cm":
			heightResult = hgtVal in range(150,193+1)
		elif hgtTyp == "in":
			heightResult = hgtVal in range(59,76+1)
		else:
			heightResult = False

		pattern = re.compile("[A-Za-z0-9]+")
		hairResult = hcl[0] == "#" and pattern.fullmatch(hcl[1:]) is not None and len(hcl) == 7

		pidResult = len(entry['pid']) == 9
		eclCheck = ecl in ["amb","blu" ,"brn" ,"gry" ,"grn" ,"hzl" ,"oth"]
			

		return ExpirationResult and heightResult and hairResult and pidResult and eclCheck

	#To catch for when entries that should be ints are *not* ints
	except:
		return False


def in1to10(n, outside_mode):
	print(n in range(1,10+1))
	print(outside_mode)
	print(' ')
	return (n == 10 or(n in range(1,10+1)) != outside_mode)
	

print(in1to10(10,True))
