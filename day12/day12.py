def step1(lines):
	direction = "E"

	blaby = {"N":0,"E":0,"S":0,"W":0}
	directionHelp = ["N","E","S","W"]
	for instruction in lines:
		action = instruction[0]
		value = int(instruction[1:])

		if action == "F":
			blaby[direction] += value
		elif action in directionHelp:
			blaby[action] += value
		else:
			spinny = value // 90
			if action == "L":
				spinny = -spinny
			direction = directionHelp[(directionHelp.index(direction)+spinny)%4]
			
	return(abs(blaby["N"]-blaby["S"])+abs(blaby["E"]-blaby["W"]))

def step2(lines):
	waypoint = {"N":1,"E":10,"S":0,"W":0}
	blaby = {"N":0,"E":0,"S":0,"W":0}

	for instruction in lines:
		action = instruction[0]
		value = int(instruction[1:])
		
		if action == "F":
			for way in waypoint.keys():
				if waypoint[way] != 0:
					blaby[way] += waypoint[way] * value
		elif action in ["N","E","W","S"]:
			waypoint[action] += value
		else:
			spinny = value // 90
			if action == "R":
				spinny = -spinny
			spinHelp = [waypoint["N"],waypoint["E"],waypoint["S"],waypoint["W"]]
			spinHelp = spinHelp[spinny:] + spinHelp[:spinny]
			waypoint["N"],waypoint["E"],waypoint["S"],waypoint["W"] = spinHelp[0],spinHelp[1],spinHelp[2],spinHelp[3]

	return(abs(blaby["N"]-blaby["S"])+abs(blaby["E"]-blaby["W"]))
	
def main():
	with open("input.txt") as inputfile:
		lines = inputfile.read().splitlines()
		print(step1(lines))
		print(step2(lines))
main()