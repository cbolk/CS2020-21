# Write a program that receives in input the name of a file containng the length 
# of neurons, and computes and outputs the minimal, maximum, average and standard 
# deviation of the values.

fname = raw_input()

fin = open(fname, "r")
neurons = []

line = fin.readline()
val = float(line)
minl = val
maxl = val
totl = val 
num = 1
neurons.append(val)
for line in fin:
	val = float(line)
	if val > maxl:
		maxl = val
	elif val < minl:
		minl = val
	neurons.append(val)
	totl = totl + val
	num += 1
fin.close()
