ADENINE = 'A'
CYTOSINE = 'C'
GUANINE = 'G'
THYMINE = 'T'

sequence = input()

nA = sequence.count(ADENINE)
nC = sequence.count(CYTOSINE)
nG = sequence.count(GUANINE)
nT = sequence.count(THYMINE)
size = len(sequence)

print(nA, nC, nG, nT, size)

#GC-content
gc = float(nG+nC)/(nA+nT+nG+nC)

#AT/GC ratio
atgc = float(nA+nT)/(nG+nC)

print("GC-ratio: {0:.2f}%".format(gc*100))
print("AT/GC-ratio: {0:.2f}%".format(atgc*100))
