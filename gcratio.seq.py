ADENINE = 'A'
CYTOSINE = 'C'
GUANINE = 'G'
THYMINE = 'T'

DNAELEM = ADENINE + CYTOSINE + GUANINE + THYMINE
nDNAElem = len(DNAELEM)
countElem = [0,0,0,0]

sequence = input()

j = 0
for i in DNAELEM:
	countElem[j] = sequence.count(i)
	print(str(countElem[j]), end=' ')
	j = j + 1

size = len(sequence)
print(size)

tot = sum(countElem)	

#GC-content
gc = float(countElem[1]+countElem[2])/(tot)

#AT/GC ratio
atgc = float(countElem[0]+countElem[3])/(countElem[1]+countElem[2])

print("GC-ratio: {0:.2f}%".format(gc*100))
print("AT/GC-ratio: {0:.2f}%".format(atgc*100))
