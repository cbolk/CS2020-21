STOP = 0

maxSeq = 0
oldValue = float(raw_input())
if oldValue != STOP:
	#first growing sequence
	maxSeq = 1
	n = float(raw_input())
	while n != STOP and n > oldValue:
		maxSeq = maxSeq + 1
		oldValue = n
		n = float(raw_input())
	#subsequent sequences
	curSeq = 0
	oldValue = n
	n = float(raw_input())
	while n != STOP:
		if n > oldValue:
			curSeq = curSeq + 1
		else:
			if curSeq > maxSeq:
				maxSeq = curSeq
			curSeq = 0
		oldValue = n
		n = float(raw_input())
else:
	maxSeq = 0

print(str(maxSeq))