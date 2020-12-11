<<<<<<< HEAD
def main():
	with open("input2.txt","r") as inputfile:
		numslist = inputfile.read().splitlines()
		for i in numslist:
			for j in numslist:
				for k in numslist:
					if int(i) + int(j) + int(k) == 2020:
						print("We got " + i + " and " + j + " and " + k +"! Result is: " + str(int(i)*int(j)*int(k)))
						#return int(i)*int(j)*int(k)


def improvement(inputCount,desiredResult):
	with open("input2.txt","r") as inputfile:
		numslist = inputfile.read().splitlines()
		numslist = list(map(int,numslist))

		keyList = [0] * inputCount
		index = 0

		while(index < (len(numslist)**inputCount)):
			valueList = []
			for key in keyList:
				valueList.append(numslist[key])
			print(valueList)
			index += 1 




		# numslist.sort()
		# print(recursiveFunction(count=0,stop=inputCount,desiredResult=desiredResult,currentList=[],fullList=numslist,index=0))




# def recursiveFunction(count,stop,desiredResult,currentList,fullList,index):
# 	print(currentList)
# 	if count<stop:
# 		currentList.append(fullList[index])
# 		result = recursiveFunction(count+1,stop,desiredResult,currentList,fullList,index)
# 		if result != 0:
# 			return result
# 		index +=
# 	else:
# 		if sum(currentList) == desiredResult:
# 			print("Wahoo!")
# 			return currentList
# 		print("returning..")
# 		print("")
# 		return 0

=======
def main():
	with open("input2.txt","r") as inputfile:
		numslist = inputfile.read().splitlines()
		for i in numslist:
			for j in numslist:
				for k in numslist:
					if int(i) + int(j) + int(k) == 2020:
						print("We got " + i + " and " + j + " and " + k +"! Result is: " + str(int(i)*int(j)*int(k)))
						#return int(i)*int(j)*int(k)


def improvement(inputCount,desiredResult):
	with open("input2.txt","r") as inputfile:
		numslist = inputfile.read().splitlines()
		numslist = list(map(int,numslist))

		keyList = [0] * inputCount
		index = 0

		while(index < (len(numslist)**inputCount)):
			valueList = []
			for key in keyList:
				valueList.append(numslist[key])
			print(valueList)
			index += 1 




		# numslist.sort()
		# print(recursiveFunction(count=0,stop=inputCount,desiredResult=desiredResult,currentList=[],fullList=numslist,index=0))




# def recursiveFunction(count,stop,desiredResult,currentList,fullList,index):
# 	print(currentList)
# 	if count<stop:
# 		currentList.append(fullList[index])
# 		result = recursiveFunction(count+1,stop,desiredResult,currentList,fullList,index)
# 		if result != 0:
# 			return result
# 		index +=
# 	else:
# 		if sum(currentList) == desiredResult:
# 			print("Wahoo!")
# 			return currentList
# 		print("returning..")
# 		print("")
# 		return 0

>>>>>>> 93e4f3d50c9370b0629b0c3b5cc1471c859e1289
improvement(2,2020)