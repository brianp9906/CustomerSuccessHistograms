# histGrapher takes as input the data array, the data stats dictionary, the frequency array, and the bin array

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# Define the alpha value and color of bars in the histogram plot
alphaValue = 0.75
colorValue = 'purple'

def histGrapher(dataArray, statsDict, frequencyArray, binArray, title):

	# Extract mean and standard deviation from the stats dictionary
	mean = statsDict['mean']
	stdev = statsDict['stdev']

	# Figure out scale factor by multiplying number of elements in dataArray by the binSize
	scaleFactor = len(dataArray) * statsDict['binSize']

	# Implemented realBinMax to keep the graph centered around important data and not outliers
	realBinMax = binArray[len(binArray) - 2] + statsDict['binSize']

	# Use predetermined binMin and binMax from binArray instead of auto generating axis to reduce effect of outliers
	axisArray = [0, realBinMax, 0, max(frequencyArray) * 1.1]

	n, bins, patches = plt.hist(dataArray, binArray, facecolor=colorValue, alpha=alphaValue)

	# Add a 'best fit' line
	y = mlab.normpdf(bins, mean, stdev)
	z = scaleFactor * y
	l = plt.plot(bins, z, 'r--', linewidth=1)

	# Set up all the title and axis information
	plt.xlabel(title)
	plt.ylabel('Frequency')
	plt.title(r'$\mathrm{Histogram\ of\ ' + title + ':}\ \mu=' + str(round(mean, 1)) + ',\ \sigma=' + str(round(stdev,1)) + '$')
	r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$'
	plt.axis(axisArray)
	plt.grid(True)

	plt.show()