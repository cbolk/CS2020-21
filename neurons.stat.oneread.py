fname = raw_input()

fin = open(fname, "r")
neurons = fin.readlines()
fin.close()

val = float(neurons[0])
minl = val
maxl = val
tot = 0.0					# tot = val
num = 0						# num = 1
for elem in neurons:		# for i in range(1, numberofneurons):
	val = float(elem)
	if val > maxl:
		maxl = val
	elif val < minl:
		mixl = val
	tot = tot + val
	num += 1

