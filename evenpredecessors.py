BASE = 2

n = int(raw_input())

if n % 2 == 1:
	n = n - 1	 #if it is odd, we find the first even number to be printed
else
	n = n - 2	#if it is even, we skip the value itself

while n >= 0:
	print(str(n))
	n = n - 2
