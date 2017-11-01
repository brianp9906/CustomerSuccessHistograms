import csv, matplotlib
from binSort import frequencySort
from binStats import binStats
from fileOpener import fileOpener
from histGrapher import histGrapher

# Designate the target .csv file to parse
filename = fileOpener()
permissions = 'rwab'  # b flag may be required depending on the platform

# location of the "average" column in our LogicMonitor report .csv
averageCol = 7
binCount = 20

# Open .csv with the designated permissions and automatically detect formatting
file = open(filename, permissions)

# Initialize reader to parse file
reader = csv.reader(file)

[data, stats, title] = binStats(reader)

# Consider removing duplicate entries of datapoint names (and thus histogram names) by passing it as list(set(x))

# Initialize bins array by creating bincount number of entries that are stats['binSize'] apart
bins = []
for i in range(0,binCount):
	bins.append(i * stats['binSize'])

# Append catch all bin at the end of bins for visibility into outlier values
bins.append(max(data))

frequencyArray = frequencySort(bins,data)
print frequencyArray

histGrapher(data, stats, frequencyArray, bins, title)