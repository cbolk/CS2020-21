MAX_ITERATIONS = 10
n = float(raw_input())
max = n
max_fractional_part = n - int(n)
i = 1
while i < MAX_ITERATIONS:
	fractional_part = n - int(n)
	if fractional_part > max_fractional_part:
		max_fractional_part = fractional_part
		max = n
	i += 1
print(str(max))
print(str(max_fractional_part))