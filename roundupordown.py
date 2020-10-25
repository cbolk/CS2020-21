UP = '+'
DOWN = '-'

upOrDown = raw_input()  #it is a character
while upOrDown != UP and upOrDown != DOWN:
    upOrDown = raw_input()
    
value = float(raw_input())
valueint = int(value)
if value != float(valueint):
    if upOrDown == UP:
        roundedvalue = valueint + 1
    else:
        roundedvalue = valueint
else:
    roundedvalue = valueint

print(str(roundedvalue))
