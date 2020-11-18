#Write a function that receives in input the name of a file storing in a csv 
#format the codon amino acids correspondence and returns a dictionary, 
#having as a key the triplet and as a value the amino acid. 
#Write a function that receives in input a RNA sequence and computes and 
#returns the corresponding protein. 
#Write a program that receives in input the name of a file storing a RNA 
#sequence in the FASTA format, and the name where to save the results, 
#and computes the protein (to be saved in the file). The file containing 
#the encoding is called "codon.csv"

UNKNOWN = "*"

def loadCodonAminoDictionary(filename):
	fin = open(filename, "r")
	cadict = {}
	for line in fin:
		aline = line.strip()
		info = aline.split(",")  # ['GCU', 'A']
		triplet = info[0].upper()
		ch = info[1].upper()
		cadict[triplet] = ch
	fin.close()
	return cadict

# seq: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# output: MAM....
def getProtein(seq, codict):
	size = len(seq)
	prot = ""
	for i in range(0, size, 3):
		seqtriplet = seq[i:i+3]	#slice from index i to index i+2
		if not codict.has_key(seqtriplet):
			corr = UNKNOWN
		else:
			corr = codict.get(seqtriplet)
		prot = prot + corr
	return prot

FILENAME = "codon.csv"
codondict = loadCodonAminoDictionary(FILENAME)
rnaseq = raw_input()
protein = getProtein(rnaseq, codondict)
print(protein)