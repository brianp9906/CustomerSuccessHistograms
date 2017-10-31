import csv, statistics, plotly

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

# Initialize variables to contain datapoints from .csv and resulting statistical variables
averageValues = []
stats = {}

for idx, row in enumerate(reader):
	# Trim off top empty and header row and remove all null datapoints
	if idx > 1 and row[averageCol] != 'No Data':
		# Append all values of the "average" column to the averageValues array
		averageValues.append(float(row[7]))

# Using the now populated averageValues, fill the statistics dictionary with the required values
stats['mean'] = statistics.mean(averageValues)
stats['median'] = statistics.median(averageValues)
stats['mode'] = statistics.mode(averageValues)
stats['stdev'] = statistics.pstdev(averageValues)
stats['variance'] = statistics.variance(averageValues)
stats['max'] = max(averageValues)
stats['min'] = min(averageValues)
stats['binSize'] = (stats['mean'] - stats['min']) / (binCount / 2)

# Consider removing duplicate entries of datapoint names (and thus histogram names) by passing it as list(set(x))

# Initialize bins array by creating bincount number of entries that are stats['binSize'] apart
bins = []
for i in range(0,binCount):
	bins.append(i * stats['binSize'])

# This function takes an array of buckets and an array of data as input
# and counts the number of datapoints in each bucket to produce y-axis data for a histogram

def frequencySort(binArray, dataArray):
	bins = len(binArray)
	# Initialize frequency information to be returned
	frequencyArray = []
	for i in range(0,bins + 1):
		frequencyArray.append(0)

	for item in dataArray:
		for idx, thing in enumerate(binArray):
			# Put items from dataArray into 
			if item >= thing and item < binArray[idx + 1]:
				frequencyArray[idx] += 1
			else:
				frequencyArray[bins] += 1

	return frequencyArray


