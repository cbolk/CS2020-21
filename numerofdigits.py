BASE = 10

val = input()

ndigits = 0
while val > 0:
    ndigits = ndigits + 1
    val = val / BASE

print(ndigits)
	