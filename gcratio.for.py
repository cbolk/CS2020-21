ADENINE = 'A'
CYTOSINE = 'C'
GUANINE = 'G'
THYMINE = 'T'

sequence = input()

nA = 0
nC = 0
nG = 0
nT = 0
size = len(sequence)
for i in range(0,size):
    if sequence[i] == ADENINE:
        nA = nA + 1
    elif sequence[i] == CYTOSINE:
        nC = nC + 1
    elif sequence[i] == GUANINE:
        nG = nG + 1
    elif sequence[i] == THYMINE:
        nT = nT + 1

print(nA, nC, nG, nT, size)

#GC-content
gc = float(nG+nC)/(nA+nT+nG+nC)

#AT/GC ratio
atgc = float(nA+nT)/(nG+nC)

print("GC-ratio: {0:.2f}%".format(gc*100))
print("AT/GC-ratio: {0:.2f}%".format(atgc*100))
