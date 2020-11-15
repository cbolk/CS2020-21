FOUND = 1
NOTFOUND = 0

#similar to isAnagram
#each word can appear only once
def sameListOfWords(lst1, lst2):
    nwords1 = len(lst1)
    nwords2 = len(lst2)
    if nwords1 == nwords2:
        count = [NOTFOUND]*nwords1
        ris = True
        for word in lst1:   #for every word in first list
            found = False
            for i in range(0, nwords2): # look in second list
                if lst2[i] == word and count[i] == NOTFOUND:    # if you find it and it is the first time
                    count[i] = FOUND                            # mark it found
                    found = True
                    break
                elif lst2[i] == word and count[i] == FOUND:     # it is the second time you find it
                    ris = False
                    break
            if not found:
                ris = False     
                break           # useless to continue
        # we have already verified same length, so if all words are found, everything is ok
    else:
        ris = False
    return ris

#similar to sameListOfWords
#a character can appear more than once
def isAnagram(word1, word2):
    size1 = len(word1)
    size2 = len(word2)
    if size1 == size2:
        count = [NOTFOUND]*size1
        ris = True
        for ch in word1:
            found = False
            for i in range(0, size2):
                if word2[i] == ch and count[i] == NOTFOUND:
                    count[i] = FOUND
                    found = True
                    break # interrupt the inner loop
            if not found:
                ris = False
                break # useless to continue, interrupt the outer loop
    else:
        ris = False
    return ris

def wordsDifferByOneCharacter(word1, word2):
    size1 = len(word1)
    size2 = len(word2)
    if size1 == size2:
        ndiff = 0
        ris = True
        for i in range(0, size1):
            if word1[i] != word2[i]:
                ndiff += 1
            if ndiff == 2:  # or simply ndiff > 1
                ris = False
                break  #useless to continue
    else:
        ris = False
    return ris


def wordsDifferByOneExtraCharacter(word1, word2):
    size1 = len(word1)
    size2 = len(word2)
    if size1 == size2 + 1:
        longw = word1
        shortw = word2
        size = size2    # the shortest
        ris = True
    elif size2 == size1 + 1:
        longw = word2
        shortw = word1
        size = size1    # the shortest
        ris = True
    else:
        ris = False
    if ris: 
        i = 0
        while i <  size and longw[i] == shortw[i]:
            i += 1
        if i < size:
            j = i + 1
            while i < size and longw[j] == shortw[i]:
                j += 1
                i += 1
            if i < size:    #if we stop before the end, there is something wrong
                ris = False

    return ris


fileprob =  raw_input()
filesol =  raw_input()


fp = open(fileprob, "r")
fs = open(filesol, "r")

#prepare list of words
seqprob = fp.readline().strip()
seqsol = fs.readline().strip()

words = seqprob.split(",")
wordsprob = []
for word in words:
    wordsprob.append(word.strip())

words = seqsol.split(",")
wordssol = []
for word in words:
    wordssol.append(word.strip())
    
#print(wordsprob)
#print(wordssol)

if sameListOfWords(wordsprob, wordssol):
    i = 0
    numwords = len(wordssol)
    isValid = True
    while i < numwords-1 and isValid:
#    print(wordssol[i], wordssol[i+1])
        if not isAnagram(wordssol[i], wordssol[i+1]):
            if not wordsDifferByOneCharacter(wordssol[i], wordssol[i+1]):
                if not wordsDifferByOneExtraCharacter(wordssol[i], wordssol[i+1]):
                    isValid = False
                    break
        i += 1
else:
    isValid = False
    
print (isValid)

