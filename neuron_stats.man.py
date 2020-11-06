neurons = []
val = float(raw_input())
while val != 0:
	neurons.append(val)
	val = float(raw_input())

#compute various stats

#for each element in the list
minlen = neurons[0]
maxlen = neurons[0]
totlen = 0.0
numneurons = 0
for elem in neurons:
	if minlen > elem:
		minlen = elem
	elif maxlen < elem:
		maxlen = elem
	totlen = totlen + elem
	numneurons = numneurons + 1

avglen = totlen / numneurons
middle = numneurons / 2		# numneurons // 2  in python 3
th25 = numneurons / 4		# ...
th75 = numneurons * 3 / 4	# ...
q2 = neurons[middle]
q1 = neurons[th25]
q3 = neurons[th75]

totlen = 0.0
for elem in neurons:
	totlen = totlen + (elem-avglen)**2

stddev = (totlen/numneurons)**0.5

print(str(minlen), str(maxlen), str(avglen), str(stddev), str(q1), str(q2), str(q3))
#or
print(minlen, maxlen, avglen, stddev, q1, q2, q3)
