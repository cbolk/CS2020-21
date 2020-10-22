# write a program that receives in input a positive integer and we compute
# and output True if it is an even value, False otherwise

val = int(raw_input())
if val % 2 == 0:
	iseven = True
else:
	iseven = False

print(str(iseven))


val = int(raw_input())				# 0 means False ... != 0  means True
if val % 2 != 0:						# if val % 2: 
	iseven = False
else:
	iseven = True

print(str(iseven))