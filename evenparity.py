BASE = 2
ODD_PARITY = 1
EVEN_PARITY = 0

parity = EVEN_PARITY

n = int(raw_input())
number01s = 0 

while n > 0:
	remainder = n % BASE
	number01s = number01s + remainder
	n = n / BASE

parityBit = (number01s + parity) % BASE
print(parityBit)