DNACOMPLEMENT = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A', 'a' : 't', 'c' : 'g', 'g' : 'c', 't' : 'a'}

# compl = DNACOMPLEMENT.get(ch)


def computeReverseComplement(seq):
    revseq = ""
    size = len(seq)
    for i in range(size-1,-1,-1):    #i = size - 1  while i >= 0:   i = i - 1
        ch = seq[i]
        compl = DNACOMPLEMENT.get(ch)
        revseq = revseq + compl
    
    return revseq


def isPalindrome4matching(seq):
	#seq  CACGTG
	revcomp = computeReverseComplement(seq)
	#revcomp   CACGTG
	size = len(revcomp)
	for i in range(0, size):
		if seq[i] != revcomp[i]:
			return False
    
	return True


# CACGTG

inseq = raw_input()
ris = isPalindrome4matching(inseq)
print(ris)