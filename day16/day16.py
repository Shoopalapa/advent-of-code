def step1(lines):
	ranges = []
	nearbyTickets = []
	for line in lines[0].split("\n"):
		options = line.split(": ")[1]
		optionsParsed = options.split(" or ")
		
		for option in optionsParsed:
			rangeParsed = option.split("-")
			ranges.extend(list(range(int(rangeParsed[0]),int(rangeParsed[1])+1)))

	total = 0
	for line in lines[2].split("\n")[1:]:
		for num in line.split(","):
			numInt = int(num)
			if numInt not in ranges:
				total += numInt

	return(total)

def step2(lines):
	pass 
	
def main():
	with open("input.txt") as inputfile:
		lines = inputfile.read().split("\n\n")
		print(step1(lines))

main()