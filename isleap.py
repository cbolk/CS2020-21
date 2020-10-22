# write a program that receives in input a positive integer
# and computes and outputs True if it is a leap year, 
# False otherwise

year = int(raw_input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
	isleap = True
else:
	isleap = False

print(str(isleap))
