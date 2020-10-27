userX = float(raw_input())
userY = float(raw_input())

num = int(raw_input())
pointX = float(raw_input())
pointY = float(raw_input())
topTemp = float(raw_input())
minSqDist = (pointX - userX)**2 + \
			(pointY - userY)**2
cont = 1
while cont < num:
	pointX = float(raw_input())
	pointY = float(raw_input())
	pointTemp = float(raw_input())
	sqDist = (pointX - userX)**2 + \
			(pointY - userY)**2
	if sqDist < minSqDist:
		minSqDist = sqDist
		if pointTemp > topTemp:
			topTemp = pointTemp
	cont = cont + 1
