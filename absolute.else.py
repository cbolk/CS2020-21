# write a program that receives an integer and 
# computes and outputs its absolute value

val = int(raw_input())
if val < 0:					#  if val > 0:
	abs_val = -val  		#	  abs_val = val
else:						#  else:	
	abs_val = val           #	  abs_val = -val

print(str(abs_val))
