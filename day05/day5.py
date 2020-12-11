<<<<<<< HEAD
def main():
	with open("input.txt") as inputfile:
		seats = inputfile.read().splitlines()

		maxID = 0
		gah = []

		for i in range(1,113):
			for j in range(0,8):
				gah.append((i*8)+j)

		for seat in seats:

			rowRange = list(range(0,127+1))
			columnRange = list(range(0,7+1))

			rowID = seat[:-3]
			columnID = seat[-3:]

			for identifier in rowID:
				if identifier == "F":
					rowRange = rowRange[:(len(rowRange)//2)]
				else:
					rowRange = rowRange[(len(rowRange)//2):]

			for identifier in columnID:
				if identifier == "L":
					columnRange = columnRange[:(len(columnRange)//2)]
				else:
					columnRange = columnRange[(len(columnRange)//2):]

			maxTest = (rowRange[0] * 8) + columnRange[0]
			if maxTest > maxID:
				maxID = maxTest
		
			try:
				gah.remove(maxTest)
			except:
				pass

		print(gah)

=======
def main():
	with open("input.txt") as inputfile:
		seats = inputfile.read().splitlines()

		maxID = 0
		gah = []

		for i in range(1,113):
			for j in range(0,8):
				gah.append((i*8)+j)

		for seat in seats:

			rowRange = list(range(0,127+1))
			columnRange = list(range(0,7+1))

			rowID = seat[:-3]
			columnID = seat[-3:]

			for identifier in rowID:
				if identifier == "F":
					rowRange = rowRange[:(len(rowRange)//2)]
				else:
					rowRange = rowRange[(len(rowRange)//2):]

			for identifier in columnID:
				if identifier == "L":
					columnRange = columnRange[:(len(columnRange)//2)]
				else:
					columnRange = columnRange[(len(columnRange)//2):]

			maxTest = (rowRange[0] * 8) + columnRange[0]
			if maxTest > maxID:
				maxID = maxTest
		
			try:
				gah.remove(maxTest)
			except:
				pass

		print(gah)

>>>>>>> 93e4f3d50c9370b0629b0c3b5cc1471c859e1289
main()