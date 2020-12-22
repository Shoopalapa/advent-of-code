## Learned to use the eval function from Strilanc's comment in https://www.reddit.com/r/adventofcode/comments/kfeldk/2020_day_18_solutions/ and gave me the idea to use a class
def step1(lines):
	total = 0
	for expression in lines:


	return(total)

def main():
	with open("inputtest.txt") as inputfile:
		lines = inputfile.read().splitlines()
		print(step1(lines))

main()
