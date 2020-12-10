import matplotlib.pyplot as plt
import numpy as np

FREQ = 360 #Hz	60 numbers in 1 second
SECSINMIN = 60

def findpeaks(x, mph):
#	mph = 1.2
#	mingap = 0.2
	nelem = len(x)
	ndiff = nelem-1
	diff = []
	for i in range(0, ndiff):
	    diff.append(float(x[i+1] - x[i]))
	#print(x)
	#print(diff)
	rising = diff[:]
	rising.insert(0,0)
	decreasing = diff[:]
	decreasing.append(0)

	peaks = []
	for i in range(0, nelem):
	    if(rising[i] > 0 and decreasing[i] <= 0):   # = to keep first of a plateau
	        peaks.append(i)
	#print(peaks, len(peaks))
	#peaks higher than minimumpeakheight mph
	for p in reversed(peaks):
	    if x[p] < mph:
	        peaks.remove(p)
	#print(peaks)
	return peaks
	#print(peaks, len(peaks))

	# #peaks higher than surrounding gap
	# for i in range(npeaks-1,-1,-1):
	#     if not(abs(x[peaks[i]] - x[peaks[i]-1]) > mingap and abs(x[peaks[i]] - x[peaks[i]+1]) > mingap):
	#         # to keep first of a plateau
	#         if not (abs(x[peaks[i]] - x[peaks[i]-1]) > mingap and x[peaks[i]] == x[peaks[i]+1]):
	#             peaks.remove(peaks[i])



## main process
fname = input()	#raw_input()

try:
	fin = open(fname, "r")
	x = fin.readlines()
	points = []
	for elem in x:
		points.append(float(elem))
	fin.close()
	npoints = len(points)

	maxtime = npoints / FREQ
	#timeline
	timelinesec = list(np.linspace(0, maxtime, npoints))
#	print(timelinesec)
	timeline = []
	for t in timelinesec:
		timeline.append(t/(FREQ))

#	print(timeline)

	minpeakheight = float(input())
	allpeaks = findpeaks(points, minpeakheight)

	# REMOVE NEGATIVE PEAKS
	peaklist = []
	for i in allpeaks:
		if points[i] >= 0.0:
			peaklist.append(i)
	npeaks = len(peaklist)

	### tachogram
	# distance between peaks
	rri = [np.nan]

	i = 1
	while(i < npeaks):
		rri.append(abs(peaklist[i]-peaklist[i-1])/FREQ)
		i += 1

#	print(rri)

	#plot
	_, ax = plt.subplots(1, 1, figsize=(8, 4))
	no_ax = True
	#plot values
	ax.plot(points, 'b', lw=1)
	label = 'peak'
	label = label + 's' if npeaks > 1 else label
	#plot peaks
	ax.plot(peaklist, [points[i] for i in peaklist], '.', mfc=None, mec='r', mew=2, ms=8,label='%d %s' % (npeaks, label))
	ax.plot(peaklist, rri, mfc=None, mec='r', mew=2, ms=8, label="RR interval", color="#e8a241")
	ax.legend(loc='best', framealpha=.5, numpoints=1)
	ax.set_xlim(-.02*npoints, npoints*1.02-1)
	ymax = max(rri[1:])
	if max(points) > ymax:
		ymax = max(points)
	ymin = min(points)
	if ymax > ymin:
		yrange = ymax - ymin
	else:
		yrange = 1
	ax.set_ylim(ymin - 0.1*yrange, ymax + 0.1*yrange)
	xlabels = ['{:,.2f}'.format(xl) for xl in ax.get_xticks()/FREQ]
	ax.set_xticklabels(xlabels)
	ax.set_xlabel('Time (sec)', fontsize=12)
	ax.set_ylabel('Amplitude', fontsize=12)
	plt.title("ECG")
	plt.show()

except FileNotFoundError:
	print("Impossible to access file " + fname)
