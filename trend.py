# write a program that receives in input an integer value and
# computes and outputs '/' if the value is positive, '-' if the value is 0
# '\' otherwise

POS = '/'
NEG = '\\'
ZERO = '-'

val = int(raw_input())
if val > 0:
	sOut = POS
else:
	if val == 0:			# if val < 0:
		sOut = ZERO			# 	 sOut = NEG
	else:					# else:
		sOut = NEG			#	 sOut = ZERO

print(sOut)

