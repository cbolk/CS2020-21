# write a program that receives in input an integer value and
# computes and outputs '/' if the value is positive, '-' if the value is 0
# '\' otherwise

POS = '/'
NEG = '\\'
ZERO = '-'

val = int(raw_input())
if val > 0:
	sOut = POS
elif val == 0:
	sOut = ZERO
else:
	sOut = NEG

print(sOut)