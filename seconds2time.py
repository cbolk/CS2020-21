# write a program that receives in input a strictly positive 
# integer (and it is surely so) which represents an amount of 
# time expressed in seconds. The program computes and outputs 
# this same amount expressed in hours, minutes and seconds.

# 200
# 200s = 0h 3m 20s

SEC_IN_MIN = 60
MIN_IN_HOUR = 60

time = int(raw_input())		# time = input()
hours = time / (SEC_IN_MIN * MIN_IN_HOUR)
remainingtime = time % (SEC_IN_MIN * MIN_IN_HOUR)
minutes = remainingtime / SEC_IN_MIN
seconds = remainingtime % SEC_IN_MIN

strOut = str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"

print(strOut)