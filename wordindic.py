FILENAME = "dictionary.txt"
word = raw_input()

fin = open(FILENAME, "r")

for line in fin:
    line = line.strip()
    if line.upper() < word.upper():
    	print(line)
        continue
    elif line.upper() == word.upper():
        found = True
        break
    else:
        found = False
        break
fin.close()
print(found)
