import csv, statistics, plotly
from binSort import frequencySort
from binStats import binStats

# Designate the target .csv file to parse
filename = 'alertsPerDevice.csv'
permissions = 'rwab'  # b flag may be required depending on the platform

# location of the "average" column in our LogicMonitor report .csv
averageCol = 7
binCount = 20

# Open .csv with the designated permissions and automatically detect formatting
file = open(filename, permissions)

# Initialize reader to parse file
reader = csv.reader(file)

[data, stats] = binStats(reader)

# Consider removing duplicate entries of datapoint names (and thus histogram names) by passing it as list(set(x))

# Initialize bins array by creating bincount number of entries that are stats['binSize'] apart
bins = []
for i in range(0,binCount):
	bins.append(i * stats['binSize'])

frequencyArray = frequencySort(bins,data)
print frequencyArray

