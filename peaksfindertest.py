import matplotlib.pyplot as plt

def findpeaks(x, mph):
#  mph = 1.2
#  mingap = 0.2
   nelem = len(x)
   ndiff = nelem-1

   peaks = []
   if mph is None:
      i = 1
      while i < ndiff:
         if x[i] > x[i-1]:
            if x[i] > x[i+1]:
               peaks.append(i)
            elif x[i] == x[i+1]:
               lenplateau = 2
               while x[i] == x[i+lenplateau]:
                  lenplateau += 1
               if x[i] > x[i+lenplateau]:
                  peaks.append(i)
               i = i + lenplateau - 1
         i += 1
   else:
      i = 1
      while i < ndiff:
         if x[i] > mph and x[i] > x[i-1]:
            if x[i] > x[i+1]:
               peaks.append(i)
            elif x[i] == x[i+1]:
               lenplateau = 2
               while x[i] == x[i+lenplateau]:
                  lenplateau += 1
               if x[i] > x[i+lenplateau]:
                  peaks.append(i)
               i = i + lenplateau - 1
         i += 1

   #peaks higher than minimumpeakheight mph
#  if not mph is None: 
#     for p in reversed(peaks):
#        if x[p] < mph:
#           peaks.remove(p)
   return peaks


def findpeaksCaTa(values, mph): # 'values' is a list, 'mph' is a float
    size = len(values)
    listOfPeaks = [] 
    for i in range(1, size - 1): 
        preval = values[i - 1]
        val = values[i]
        nextval = values[i + 1]
        if val > preval and val > nextval and val > mph:
           listOfPeaks.append(i)
        else:
            continue 
            
    return listOfPeaks

def findpeaksBC(seq, mph):
    size = len(seq)
    if size > 2:
        peaks = []
        for n in range(1, size-1):
            value = float(seq[n])
            preval = float(seq[n-1])
            nextval = float(seq[n+1])
            diff_prev = value - preval
            diff_next = value - nextval
            if (value > preval) and (value >= nextval):
                if mph == 0:
                    peaks.append(n)
                elif (diff_prev >= mph) and (diff_next >= mph or diff_next == 0):
                    peaks.append(n)
    else:
        peaks = "Input not compliant"      
    return peaks

def findpeaksCP(vals, thr):
    lenv = len(vals)
    listpeaks = []
    if thr != None :
        thr = float(thr)
        for i in range(1, lenv):
            if vals[i] > vals[i-1] and vals[i] > vals[i+1] and vals[i] >= thr:
                listpeaks.append(i) 
            else :
                continue
    else :
        for i in range(1, lenv):
            if vals[i] > vals[i-1] and vals[i] > vals[i+1] :
                listpeaks.append(i)
            else :
                continue
    return listpeaks

def findpeaksPD(list_in,thres):
    length = len(list_in)
    list_of_peaks = []
    if thres == None:
        for i in range(1, length - 2):
            if list_in[i] > list_in[i - 1]:
                if list_in[i] >= list_in[i + 1]:
                    list_of_peaks.append(i)
    else:
        for i in range(1, length - 2):
            if list_in[i] > thres:
                if list_in[i] > list_in[i - 1]:
                    if list_in[i] >= list_in[i + 1]:
                        list_of_peaks.append(i)
    return list_of_peaks


def findpeaksCR(val,mph):
    peak=[]
    len_val=len(val)-1 
    for i in range(1,len_val): 
      diff_p= abs(val[i]-val[i-1])
      diff_s=abs(val[i]-val[i+1])
      if diff_p >0 and diff_s >0:
         if mph==None:
             peak.append(i)   
         elif val[i]>mph:
             peak.append(i)  
      i=i+1
    return peak
      
def findpeaksMD(finlist, mph):
#returns a list of positions of the peaks in the input file    
    peaks=[]
    l=len(finlist)
    if mph == None:
        for i in range(1,l-1):
            peaks.append(finlist[i])
        
    else:
        for i in range(1,l-1):
            valueafter=finlist[i+1]+mph
            valuebefore=finlist[i-1]+mph
            if finlist[i]>=valueafter and finlist[i]>=valuebefore and finlist[i]>=mph:   
                peaks.append(i)
                         
    return peaks

def findpeaksMM(values,mph):
    peaks=[]
    size=len(values)
    for i in range(1,size-1):
        if values[i]>values[i-1] and values[i]>=values[i+1] and values[i]>mph:
            peaks.append(i)
    return peaks


def findpeaksAP(list, mph):
    import math
    output = []
    l = len(list)
    for i in range(1, l-1):
        if list[i] == list[i + 1]:
            j = i
            while list[i]==list[i+1]:
                i=+1    
            if list[i + 1] < list[i] and list[i]>mph:
                output.append(j)
                break
            else:
                continue                  
        elif abs(list[i-1] < list[i]) and abs(list[i] > list[i+1]) and list[i] > mph:        
            output.append(i)
        else:
            continue
    return output      

def findpeaksMMT(list_input, mph): 
    list_output=[]
    if mph == None: 
        mph = 0
    else:
        mph = float(mph)
    n = len(list_input)
        #effective peaks
    for element in range(1,n-1):
        diffprevious = list_input[element] - list_input[element - 1]
        diffnext = list_input[element] - list_input[element + 1]
        if diffprevious > mph and diffnext > mph:
            list_output.append(int(element))
        
        #plateau
        elif diffprevious > mph and diffnext == 0:
            list_output.append(int(element))
        
    return list_output


def findpeaksBF(listinput, mph):
   size = len(listinput)
   list_peaks = []
   if mph == None:
      for element in range(1,size-1):
         if listinput[element] >= listinput[element+1] and \
            listinput[element] > listinput[element-1]:
            list_peaks.append(element)
   else: 
      for element in range(1,size-1):
         if listinput[element] >= listinput[element+1] and \
            listinput[element] > listinput[element-1] and listinput[element] >= mph:
            list_peaks.append(element)
       
   return list_peaks

def findpeaksCG(lst, mph):
    peaks = []
    size = len(lst) - 1
    i = 1
    for n in range(1, size):
        if mph == 'None':
            for n in range(1, size):
                if lst[n]>lst[n - 1] and lst[n]>=lst[n + 1]:
                    peaks.append(i)
                i+=1
        else:
            for n in range(1, size):
                if lst[n]>mph and lst[n]>=lst[n-1] and lst[n]>=lst[n+1]:
                    peaks.append(i)
                i+=1
    return peaks

def findpeaksMS(values, thr):
   l = len(values)
   peakvalues = []
   for i in range(0, l-2):
      if values[i+1] > values[i] and values[i+1] > thr:
         if values[i+1] == values[i+2]:
            j = 0
            while values[i+1] == values[i+2+j]:
               j = j+1
            if values[i+1] > values[i+2+j]:
               peakvalues.append(i+1)
         elif values[i+1] > values[i+2]:
            peakvalues.append(i+1)
   return peakvalues

def findpeaksCT(values, mph):
   peaks=[]
   lenseq = len(values)
   if lenseq>2:
      oldvalue=float(values[0]) 
      value=float(values[0]) 
      newvalue=float(values[0]) 
      for i in range(1,lenseq-2):
         oldvalue=float(value) 
         value=float(newvalue)
         newvalue=float(values[i])
         #now we check for the peak
         
         if mph==0 and value>newvalue and value>oldvalue and value>mph:
            peaks.append(i)
         elif mph!=0 and value>newvalue and value>oldvalue and value>mph:
            peaks.append(i)
         elif mph==0 and value<newvalue and value<oldvalue and value>mph:
            peaks.append(i)
         elif mph!=0 and value<newvalue and value<oldvalue and value>mph:
            peaks.append(i)
         else:
            continue
#      print(peaks, mph)
#   else:
#      print(peaks, mph)  
   return peaks


def findpeaksLT( Y , mph0 ):
   if mph0 == str("None"):
      mph = 0.0
   else:
      mph = float(mph0)
   Lenght = len(Y)
   ListOfPeaks = list()
   for i in range(1 , Lenght-1):
      Previous = float(Y[i-1])
      Analyzed = float(Y[i])
      Next = float(Y[i+1])
      mphPrevious = Analyzed - Previous
      mphNext = Analyzed - Next
      if (mphPrevious > mph and mphNext > mph) and (Analyzed > Previous and Analyzed > Next) :
         ListOfPeaks.append(i)
      elif (mphPrevious > mph and mphNext >= mph) and (Analyzed > Previous and Analyzed == Next):
         ListOfPeaks.append(i)
      else:
         continue		
   return ListOfPeaks



## main process
fname = input() #raw_input()

try:
   fin = open(fname, "r")
   x = fin.readlines()
   y = []
   for elem in x:
      y.append(float(elem))
      fin.close()
   npoints = len(y)

   try:
      mph = float(input())
   except ValueError:
      mph = None

   peaklist = findpeaks(y, mph)
   npeaks = len(peaklist)

   #plot
   _, ax = plt.subplots(1, 1, figsize=(8, 4))
   no_ax = True
   #plot values
   ax.plot(y, 'b', lw=1, color='#757575')
   label = 'peak'
   label = label + 's' if npeaks > 1 else label
   #plot peaks
   ax.plot(peaklist, [y[i] for i in peaklist], '*', mec='green', mew=2, ms=8,label='%d %s' % (npeaks, label))
   ax.legend(loc='best', framealpha=.5, numpoints=1)
   #false peaks on plateau
#   ax.plot([18, 29, 67], [y[18], y[29], y[67]], marker='x', mec='r', mew=2, ms=8, linewidth=0, label='false peaks - plateau')
#   ax.plot([5, 15, 40, 57, 68], [y[5], y[15], y[40], y[57], y[68]], marker='x', mec='r', mew=2, ms=8, linewidth=0, label='false peaks - plateau')
   ax.plot([18, 29, 67], [y[18], y[29], y[67]], marker='x', mec='r', mew=2, ms=8, linewidth=0, label='false peaks - plateau')
   ax.legend(loc='best', framealpha=.5, numpoints=1)

#   ax.plot([34, 55, 75], [y[34], y[55], y[75]], marker='+', mec='#3F51B5', mew=2, ms=8, linewidth=0, label='possibly missing peaks')
#   ax.plot([18, 75], [y[18], y[75]], marker='+', mec='#3F51B5', mew=2, ms=8, linewidth=0, label='possibly missing peaks')
   ax.plot([34, 55], [y[34], y[55]], marker='+', mec='#3F51B5', mew=2, ms=8, linewidth=0, label='possibly missing peaks')
   ax.legend(loc='best', framealpha=.5, numpoints=1)

   ax.set_xlim(-.02*npoints, npoints*1.02-1)
   ymin, ymax = min(y), max(y)
   yrange = ymax - ymin if ymax > ymin else 1
   ax.set_ylim(ymin - 0.1*yrange, ymax + 0.1*yrange)
   ax.set_xlabel('Data #', fontsize=14)
   ax.set_ylabel('Amplitude', fontsize=14)
   plt.title('Mixed values')
   plt.show()

   print("-------------------------------------------------------------------")
   print(peaklist)
   print("-------------------------------------------------------------------")


   pCaTa = findpeaksCaTa(y, mph)
   diff = [item for item in peaklist if item not in pCaTa]
   diff.extend([item for item in pCaTa if item not in peaklist])
   print("CaTa|01: " + str(len(diff)) + "> " + str(diff))
#   print(pCaTa)

   pBC = findpeaksBC(y, mph)
   diff = [item for item in peaklist if item not in pBC]
   diff.extend([item for item in pBC if item not in peaklist])
   print("BC|02: " + str(len(diff)) + "> " + str(diff))
#   print(pBC)

   pPD = findpeaksPD(y, mph)
   diff = [item for item in peaklist if item not in pPD]
   diff.extend([item for item in pPD if item not in peaklist])
   print("PD|03: " + str(len(diff)) + "> " + str(diff))
#   print(pPD)

   pCR = findpeaksCR(y, mph)
   diff = [item for item in peaklist if item not in pCR]
   diff.extend([item for item in pCR if item not in peaklist])
   print("CR|04: " + str(len(diff)) + "> " + str(diff))
#   print(pCR)

   pMD = findpeaksMD(y, mph)
   diff = [item for item in peaklist if item not in pMD]
   diff.extend([item for item in pMD if item not in peaklist])
   print("MD|05: " + str(len(diff)) + "> " + str(diff))
#   print(pMD)

   pMM = findpeaksMM(y, mph)
   diff = [item for item in peaklist if item not in pMM]
   diff.extend([item for item in pMM if item not in peaklist])
   print("MM|06: " + str(len(diff)) + "> " + str(diff))
#   print(pMM)

   pCP = findpeaksCP(y, mph)
   diff = [item for item in peaklist if item not in pCP]
   diff.extend([item for item in pCP if item not in peaklist])
   print("CP|07: " + str(len(diff)) + "> " + str(diff))
#   print(pCP)

   pAP = findpeaksAP(y, mph)
   diff = [item for item in peaklist if item not in pAP]
   diff.extend([item for item in pAP if item not in peaklist])
   print("AP|08: " + str(len(diff)) + "> " + str(diff))
#   print(pAP)

   pMMT = findpeaksMMT(y, mph)
   diff = [item for item in peaklist if item not in pMMT]
   diff.extend([item for item in pMMT if item not in peaklist])
   print("MMT|09: " + str(len(diff)) + "> " + str(diff))
#   print(pMMT)

   pCG = findpeaksCG(y, mph)
   diff = [item for item in peaklist if item not in pCG]
   diff.extend([item for item in pCG if item not in peaklist])
   print("CG|10: " + str(len(diff)) + "> " + str(diff))
#   print(pCG)

   pBF = findpeaksBF(y, mph)  
   diff = [item for item in peaklist if item not in pBF]
   diff.extend([item for item in pBF if item not in peaklist])
   print("BF|11: " + str(len(diff)) + "> " + str(diff))
#   print(pBF)

   pMS = findpeaksMS(y, mph)
   diff = [item for item in peaklist if item not in pMS]
   diff.extend([item for item in pMS if item not in peaklist])
   print("MS|12: " + str(len(diff)) + "> " + str(diff))
#   print(pMS)

   pCT = findpeaksCT(y, mph)
   diff = [item for item in peaklist if item not in pCT]
   diff.extend([item for item in pCT if item not in peaklist])
   print("CT|13: " + str(len(diff)) + "> " + str(diff))
#   print(pCT)

   pLT = findpeaksLT(y, mph)
   diff = [item for item in peaklist if item not in pLT]
   diff.extend([item for item in pLT if item not in peaklist])
   print("LT|14: " + str(len(diff)) + "> " + str(diff))
#   print(pLT)

   print(y)

except FileNotFoundError:
	print("Impossible to access file " + fname)

