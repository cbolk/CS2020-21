F = open('rnaseq.FASTA')
Out = open('protein_seq.fasta','w')

seq = ''
for line in F:
   if line[0] == '>':
      header = line.split()
      geneID = header[0]
      Out.write(geneID + '_protein\n')
   else:
      seq = seq + line.strip()

codonAMINO =  {   'GCU':'A','GCC':'A','GCA':'A', 'GCG':'A',
                  'CGU':'R','CGC':'R','CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 
            'AAU':'N','AAC':'N',
            'GAU':'D','GAC':'D',
            'UGU':'C','UGC':'C',
            'CAA':'Q','CAG':'Q',
            'GAA':'E','GAG':'E',
                  'GGU':'G','GGC':'G','GGA':'G', 'GGG':'G', 
            'CAU':'H','CAC':'H',
            'AUU':'I','AUC':'I', 'AUA':'I',
                  'UUA':'L','UUG':'L','CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
            'AAA':'K','AAG':'K',
            'AUG':'M',
            'UUU':'F','UUC':'F',
            'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
            'UCU':'S','UCC':'S','UCA':'S','UCG':'S','AGU':'S', 'AGC':'S', 
            'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
         'UGG':'W', 
         'UAU':'Y', 'UAC':'Y',
         'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
         'UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP' }

prot = ''
# Repeat 3 times (one per frame)
for j in range(3):
   # Insert a separator between frames
   Out.write(str(j) + "-frame\n")
   # Start from the first, second, third position
   for i in range(j,len(seq),3):
      if codonAMINO.has_key(seq[i:i+3]):
         prot = prot + codonAMINO[seq[i:i+3]]
      else:  
         prot = prot + '*'
   Out.write(prot + '\n')
   prot = ''
