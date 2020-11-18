Name,Abbr.,Molecular Weight,Molecular Formula,Residue Formula,Residue Weight,pKa,pKb,pKx,pl 
Alanine,Ala,A,89.10,C3H7NO2,C3H5NO,71.08,2.34,9.69,–,6.00 
Arginine,Arg,R,174.20,C6H14N4O2,C6H12N4O,156.19,2.17,9.04,12.48,10.76 
Asparagine,Asn,N,132.12,C4H8N2O3,C4H6N2O2,114.11,2.02,8.80,–,5.41 
Aspartic acid,Asp,D,133.11,C4H7NO4,C4H5NO3,115.09,1.88,9.60,3.65,2.77

aminodict = {'ALA' : 'A', 'ARG' : 'R', ...}

def loadAminoDictionary(filename):
	fin = open(filename, "r")	
	# read
    header = fin.readline()
    aadict = {}
    for line in fin:
    	aminoline = line.strip()
    	aminoinfo = aminoline.split(",")  ## aminoinfo = line.strip().split(",")
    	# aminoinfo = ['Alanine', 'Ala', 'A', 89.10, 'C3...']
    	triplet = aminoinfo[1].upper()
    	ch = aminoinfo[2]
    	aadict[triplet] = ch 
    	# aadict[aminoinfo[1].upper()] = aminoinfo[2]
	fin.close()
	return aadict


def loadAminoDictionaryFull(filename):
	fin = open(filename, "r")	
	# read
    header = fin.readline()
    aadict = {}
    for line in fin:
    	aminoline = line.strip()
    	aminoinfo = aminoline.split(",")  ## aminoinfo = line.strip().split(",")
    	# aminoinfo = ['Alanine', 'Ala', 'A', 89.10, 'C3...']
    	triplet = aminoinfo[1].upper()
    	ch = aminoinfo[2]
    	aadict[triplet] = aminoinfo
    	# aadict[aminoinfo[1].upper()] = aminoinfo[2]
	fin.close()
	return aadict


def loadAminoDictionaryShortAndFull(filename):
	fin = open(filename, "r")	
	# read
    header = fin.readline()
    aadict = {}
    fulldict = {}
    for line in fin:
    	aminoline = line.strip()
    	aminoinfo = aminoline.split(",")  ## aminoinfo = line.strip().split(",")
    	# aminoinfo = ['Alanine', 'Ala', 'A', 89.10, 'C3...']
    	triplet = aminoinfo[1].upper()
    	ch = aminoinfo[2]
    	aadict[triplet] = ch
    	fulldict[triplet] = aminoinfo
    	# aadict[aminoinfo[1].upper()] = aminoinfo[2]
	fin.close()
	return aadict, fulldict


filein = raw_input()
shortD, fullD = loadAminoDictionaryShortAndFull(finein)
print(shortD)
print(fullD)
