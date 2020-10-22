# write a program that receives in input 3 strictly positive integer values and outputs True if they correspond
# to the sizes of the sides of a right triangle

side1 = int(raw_input())
side2 = int(raw_input())
side3 = int(raw_input())

if (side1 * side1 == side2 * side2 + side3 * side3) or \
	(side2 * side2 == side1 * side1 + side3 * side3) or \
	(side3 * side3 == side2 * side2 + side1 * side1):
	isright = True
else:
	isright = False

print(str(isright))
