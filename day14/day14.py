import pprint

def step1(lines):
	mem = [0] * 9999

	for instructions in lines:
		if instructions[:4] == "mask":
			mask = instructions.split(" = ")[1]
		else:
			index = int(instructions.split("] = ")[0][4:])
			value = int(instructions.split(" = ")[1])
			mem[index] = bitmask(value,mask)

	return(sum(mem))

def step2(lines):
	mem = {}

	for instructions in lines:
		if instructions[:4] == "mask":
			mask = instructions.split(" = ")[1]
		else:
			indexBit = int2bit(int(instructions.split("] = ")[0][4:]),36)
			indexes = indexScrambler(indexBit,mask)

			value = int(instructions.split(" = ")[1])

			for tempIndex in indexes:
				mem[tempIndex] = value


	return(sum(mem.values()))

def indexScrambler(inputBit, mask):
	indexMask = ""

	for val, mas in zip(list(inputBit), list(mask)):
		if mas == "0":
			indexMask += val
		elif mas == "1":
			indexMask += "1"
		else:
			indexMask += "X"

	permList = []
	for perms in range(2**(indexMask.count("X"))):
		permList.append(int2bit(perms,indexMask.count("X")))

	indexList = [indexMask] * 2**(indexMask.count("X"))
	result = []
	for idx, perm in zip(indexList,permList):
		temp = list(idx)
		temp2 = list(perm)
		for i in range(temp.count("X")):
			temp[temp.index("X")] = temp2[0]
			temp2 = temp2[1:]
		result.append("".join(temp))

	for i in range(len(result)):
		result[i] = bit2int(result[i])
	return(result)

def int2bit(inputInt,size):
	result = ""
	for i in range(size):
		if 2**(size-1-i) <= inputInt:
			inputInt -= 2**(size-1-i)
			result += "1"
		else:
			result += "0"
	return(result)

def bit2int(inputBit):
	result = 0
	for index in range(36):
		if inputBit[index] == "1":
			result += 2**(35-index)

	return(result)

def bitmask(value,mask):

	valueBit = int2bit(value,36)

	resultBit = ""
	for val, mas in zip(list(valueBit),list(mask)):
		if mas == "1" or mas == "0":
			resultBit = resultBit + mas
		else:
			resultBit = resultBit + val

	return(bit2int(resultBit))

def main():
	with open("input.txt") as inputfile:
		lines = inputfile.read().splitlines()
		#print(step1(lines))
		print(step2(lines))

main()
