import numpy

neurons = []
val = float(raw_input())
while val != 0:
	neurons.append(val)
	val = float(raw_input())

print(neurons)

numneurons = len(neurons)
minlength = min(neurons)
maxlength = max(neurons)

avglength = numpy.mean(neurons)
stddev = numpy.std(neurons)
print(str(minlength), str(maxlength), str(avglength), str(stddev))
