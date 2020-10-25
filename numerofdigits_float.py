BASE = 10

val = input()

integer = int(val)
real = val - integer
ndigits = 0
while integer > 0:
    ndigits = ndigits + 1
    integer = integer / BASE
print(ndigits)

diff = real - int(real)
while diff > 0:
    ndigits = ndigits + 1
    real = real * BASE
    print (str(real) + " " + str(int(real)))
    diff = real - int(real)
print(ndigits)
