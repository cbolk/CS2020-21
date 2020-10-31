neurons = []
val = float(raw_input())
while val != 0:
	neurons.append(val)
	val = float(raw_input())

#debug printing
#print(neurons)

numneurons = len(neurons)
minlength = min(neurons)
maxlength = max(neurons)
avglength = float(sum(neurons)) / numneurons

tot = 0.0
for n in neurons:
	tot = tot + (n-avglength)**2

stddev = (tot/numneurons)**0.5

print(str(minlength), str(maxlength), str(avglength), str(stddev))
