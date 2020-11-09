USED = '+'
NOTUSED = ' '
FILEDICT = "dictionary.txt"

userword = raw_input()

#prepare the counter of characters ...
letter = []						#          
len1 = 0
for c in userword:
	letter.append(NOTUSED)
	len1 += 1
 
f = open(FILEDICT, "r")
for worddict in f:
    worddict = worddict.strip()
    len2 = len(worddict)
    if len1 == len2 and userword != worddict:
        isAnag = True
        i = 0
        while i < len1 and isAnag == True:
            found = False
            j = 0
            while j < len2 and not found:
                if (userword[i] == worddict[j]) and (letter[j] == NOTUSED):
                    letter[j] = USED
                    found = True
                else:
                    j += 1
            if not found:
                isAnag = False
            else:
                i += 1        
        letter = [NOTUSED]*len1
    else:
        isAnag = False
    if isAnag:
        print(worddict)
f.close()
