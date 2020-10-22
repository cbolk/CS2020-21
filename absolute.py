# write a program that receives an integer and 
# computes and outputs its absolute value

val = int(raw_input())		# val = input()
abs_val = val
if abs_val < 0:
	abs_val = -abs_val		# abs_val = -val

# abs_val contains for sure a positive value
print(str(abs_val))
