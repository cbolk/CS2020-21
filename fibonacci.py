numseq = int(raw_input())
while numseq <= 0:
    numseq = int(raw_input())

if numseq == 1:
    print(str(1))
else:
    prevalue = 1
    value = 1
    print(str(prevalue))
    print(str(value))
    cont = 2
    while cont < numseq:
        nextvalue = prevalue + value
        prevalue = value
        value = nextvalue
        print(str(nextvalue))
        cont = cont + 1
        