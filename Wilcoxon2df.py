TWOTAILED = 'TTT'
ONETAILED = 'OTT'

ALPHA05 = '0.05'
ALPHA01 = '0.01'


namein = raw_input() #"WilcoxonSRT.csv" #
nameout = raw_input() #"WSRTdf.csv"  #

try: 
	fin = open(namein, "r")
except IOError:
	print("impossible to open file " + namein)
else:
	try:
		fout = open(nameout, "w")
		fin.readline()
		fout.write("n,type,alpha,value\n")
		for line in fin: 
			# n,TTT05,TTT01,OTT05,OTT01
			# 5,NaN,NaN,0,NaN
			values = line.strip().split(",")
			fout.write(values[0] + "," + TWOTAILED + "," + ALPHA05 + "," + values[1] + "\n")
			fout.write(values[0] + "," + TWOTAILED + "," + ALPHA01 + "," + values[2] + "\n")
			fout.write(values[0] + "," + ONETAILED + "," + ALPHA05 + "," + values[3] + "\n")
			fout.write(values[0] + "," + ONETAILED + "," + ALPHA01 + "," + values[4] + "\n")	
		fout.close()
	except IOError:
		print("impossible to open file " + nameout)
	fin.close()
