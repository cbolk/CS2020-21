USED = '+'
NOTUSED = ' '
str1 = raw_input('')
str2 = raw_input('')

len1 = len(str1)
len2 = len(str2)
letter = []
for i in str1:
	letter.append(NOTUSED)

if len1 != len2:
	isAnag = False
else:
	

	isAnag = True
	i = 0
	while i < len1 and isAnag == True:
		trovato = False
		j = 0
		while (j < len2) and (trovato == False):
			if (str1[i] == str2[j]) and (letter[j] == NOTUSED):
				letter[j] = USED
				trovato = True
			else:
				j = j + 1
		if not trovato:
			isAnag = False
			#significa che il letter str1[i] non compare in str2
			#oppure e' gia' stato usato
			#quindi sappiamo che non e' un anagramma .. inutile continuare
		else:
			i = i + 1
print isAnag

