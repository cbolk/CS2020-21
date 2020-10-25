BASE = 10

numi = int(raw_input())
while numi <= 0:
    numi = int(raw_input())

tmp = numi / BASE
maxp = 1
while tmp > 0:
    maxp = maxp * BASE
    tmp = tmp / BASE
# numi 123456
# maxp 100000
pal = True
tmp = numi
while pal and tmp > 0:
    rightmost = tmp % BASE
    leftmost = tmp / maxp
    if rightmost != leftmost:
        pal = False
    else:
        tmp = tmp % BASE  
        tmp = tmp / BASE
        maxp = maxp / (BASE*BASE)   # we have removed 2 digits
print pal
