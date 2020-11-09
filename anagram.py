USED = '+'
NOTUSED = ' '
word1 = raw_input('')			# h o u s e
word2 = raw_input('')			# s h o e s

letter = []						#          
len1 = 0
for c in word1:
	letter.append(NOTUSED)
	len1 += 1

len2 = len(word2)
if len1 == len2:
	isAnag = True
	i = 0
	while i < len1 and isAnag == True:
		found = False
		j = 0
		while j < len2 and not found:
			if (word1[i] == word2[j]) and (letter[j] == NOTUSED):
				letter[j] = USED
				found = True
			else:
				j += 1
		if not found:
			isAnag = False
		else:
			i += 1
else:
	isAnag = False
print isAnag

