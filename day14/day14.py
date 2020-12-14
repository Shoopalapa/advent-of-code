def step1(lines):
	mem = [0] * 99999

	for instructions in lines:
		if instructions[:4] == "mask":
			mask = instructions.split(" = ")[1]
		else:
			index = int(instructions.split("] = ")[0][4:])
			value = int(instructions.split(" = ")[1])
			mem[index] = bitmask(value,mask)

	return(sum(mem))

def step2(lines):
	mem = [0] * 99999

	for instructions in lines:
		if instructions[:4] == "mask":
			mask = instructions.split(" = ")[1]
		else:
			index = int(instructions.split("] = ")[0][4:])
			indexes = indexScrambler(index,mask)

			value = int(instructions.split(" = ")[1])
			tempVal = bitmask(value,mask)

			for tempIndex in indexes:
				mem[tempIndex] = tempVal

	return(sum(mem))


def bitmask(value,mask):
	valueInt = int(value)
	valueBit = ""
	for i in range(36):
		if 2**(35-i) <= valueInt:
			valueInt -= 2**(35-i)
			valueBit = valueBit + "1"
		else:
			valueBit = valueBit + "0"

	resultBit = ""
	for val, mas in zip(list(valueBit),list(mask)):
		if mas == "1" or mas == "0":
			resultBit = resultBit + mas
		else:
			resultBit = resultBit + val

	resultInt = 0
	for bit in range(36):
		if resultBit[bit] == "1":
			resultInt += 2**(35-bit)

	return(resultInt)

def main():
	with open("input.txt") as inputfile:
		lines = inputfile.read().splitlines()
		print(step1(lines))

main()
