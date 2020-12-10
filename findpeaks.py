import matplotlib.pyplot as plt

def findpeaks(x, mph):
#	mph = 1.2
#	mingap = 0.2
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
#	if not mph is None: 
#		for p in reversed(peaks):
#			if x[p] < mph:
#				peaks.remove(p)
	print(peaks)
	return peaks
	#print(peaks, len(peaks))

	# #peaks higher than surrounding gap
	# for i in range(npeaks-1,-1,-1):
	#     if not(abs(x[peaks[i]] - x[peaks[i]-1]) > mingap and abs(x[peaks[i]] - x[peaks[i]+1]) > mingap):
	#         # to keep first of a plateau
	#         if not (abs(x[peaks[i]] - x[peaks[i]-1]) > mingap and x[peaks[i]] == x[peaks[i]+1]):
	#             peaks.remove(peaks[i])


## main process
fname = input() #raw_input()

try:
    fin = open(fname, "r")
    x = fin.readlines()
    points = []
    for elem in x:
        points.append(float(elem))
    fin.close()
    npoints = len(points)

    try:
        minpeakheight = float(input())
    except ValueError:
        minpeakheight = None

    peaklist = findpeaks(points, minpeakheight)
    print(peaklist)

	# REMOVE NEGATIVE PEAKS
	#peaklist = []
	#for i in allpeaks:
	#	if points[i] >= 0.0:
	#		peaklist.append(i)



	npeaks = len(peaklist)

	#plot
	_, ax = plt.subplots(1, 1, figsize=(8, 4))
	no_ax = True
	#plot values
	ax.plot(points, 'b', lw=1)
	label = 'peak'
	label = label + 's' if npeaks > 1 else label
	#plot peaks
	ax.plot(peaklist, [points[i] for i in peaklist], '+', mfc=None, mec='r', mew=2, ms=8,label='%d %s' % (npeaks, label))
	ax.legend(loc='best', framealpha=.5, numpoints=1)
	ax.set_xlim(-.02*npoints, npoints*1.02-1)
	ymin, ymax = min(points), max(points)
	yrange = ymax - ymin if ymax > ymin else 1
	ax.set_ylim(ymin - 0.1*yrange, ymax + 0.1*yrange)
	ax.set_xlabel('Data #', fontsize=14)
	ax.set_ylabel('Amplitude', fontsize=14)
	plt.show()

except FileNotFoundError:
	print("Impossible to access file " + fname)
