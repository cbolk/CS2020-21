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
