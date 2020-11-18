DNACOMPLEMENT = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A', 'a' : 't', 'c' : 'g', 'g' : 'c', 't' : 'a'}

# compl = DNACOMPLEMENT.get(ch)

# GGGGaaaaaaaatttatatatat
# CCCCttttttttaaatatatata
# atatatataaattttttttCCCC

# ata

def computeReverseComplement(seq):
    revseq = ""
    size = len(seq)
    for i in range(size-1,-1,-1):    #i = size - 1  while i >= 0:   i = i - 1
        ch = seq[i]
        compl = DNACOMPLEMENT.get(ch)
        revseq = revseq + compl
    
    return revseq


inseq = raw_input()
revcomp = computeReverseComplement(inseq)
print(revcomp)


DNALIST = [['A', 'T'], ['C', 'G'], ...]

def computeReverseComplementList(seq):
    revseq = ""
    size = len(seq)
    for i in range(size-1,-1,-1):    #i = size - 1  while i >= 0:   i = i - 1
        ch = seq[i]
        for elem in DNALIST:
            key = elem[0]
            if key == ch:
                compl = elem[1]
                break

        revseq = revseq + compl
    
    return revseq

