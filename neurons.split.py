LABELP = 'P'
LABELS = 'S'

NAMESRC = "neurons.ps.txt"
NAMEDSTP = "neurons.p.txt"   #destination file for primary neurons
NAMEDSTS = "neurons.s.txt"   #destination file for secondary neurons


fin = open(NAMESRC, 'r')
foutp = open(NAMEDSTP, 'w')
fouts = open(NAMEDSTS, 'w')
for line in fin:
    if len(line) > 1:      # line = 'P 441.462\n'
        n = line.split()   # n = ['P', '441.462']
        if n[0] == LABELP:
            foutp.write(n[1] + '\n')
        else:
            fouts.write(n[1] + '\n')
fin.close()
foutp.close()
fouts.close()

