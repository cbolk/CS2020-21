FILEDICT = "dictionary.txt"

word = raw_input()

fin = open(FILEDICT, "r")
found = False
for line in fin:
	worddict = line.strip()
	if worddict.upper() < word.upper():
		#go to the next word in the dictionary
		continue 
	elif worddict.upper() == word.upper():
		found = True
		#break
	else:
		#stop checking
		break

fin.close()
print(found)
