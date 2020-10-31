ADENINE = 'A'
CYTOSINE = 'C'
GUANINE = 'G'
THYMINE = 'T'

nA = 0
nC = 0
nG = 0
nT = 0
totsize = 0
sequence = input()
size = len(sequence)
while size > 0:
	nA = nA + sequence.count(ADENINE)
	nC = nC + sequence.count(CYTOSINE)
	nG = nG + sequence.count(GUANINE)
	nT = nT + sequence.count(THYMINE)
	totsize = totsize + size
	sequence = input()
	size = len(sequence)

#no more info in input
print(nA, nC, nG, nT, totsize)

#GC-content
gc = float(nG+nC)/(nA+nT+nG+nC)

#AT/GC ratio
atgc = float(nA+nT)/(nG+nC)

print("GC-ratio: {0:.2f}%".format(gc*100))
print("AT/GC-ratio: {0:.2f}%".format(atgc*100))
