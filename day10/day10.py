def step1(lines):

	diffs = {1:0,2:0,3:1}

	for i in range(1,len(lines)):
		localdiff = lines[i] - lines[i-1]
		diffs[localdiff] += 1
	
	return(diffs[1]*diffs[3])

# Used Reddit user '_bm's comment in https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/ to solve Step 2
def step2(lines):

	numSequence = [1] + [0] * (len(lines) -1)

	for i in range(len(lines)):
		 j = i + 1
		 while j < len(lines) and lines[j]-lines[i] <= 3:
		 	numSequence[j] += numSequence[i]
		 	j += 1
	
	return(numSequence[-1])

def main():
	with open("input.txt") as inputfile:
		lines = inputfile.read().splitlines()
		intLines = [0] + list(map(int,lines))
		intLines.sort()

		#print(step1(intLines))
		print(step2(intLines))
main()

