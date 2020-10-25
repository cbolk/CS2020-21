BASE = 10

value = int(raw_input())

if value < 0:
    absval = -value
else:
    absval = value

tot = 0
while absval > 0:
    digit = absval % BASE
    tot = tot + digit
    absval = absval / BASE

print(str(tot))
