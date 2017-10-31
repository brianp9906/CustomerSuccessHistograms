import csv, statistics, plotly

# Designate the target .csv file to parse
filename = 'alertsPerDevice.csv'
permissions = 'rwab' # b flag may be required depending on the platform
averageCol = 7 # location of the "average" column in our LogicMonitor report .csv
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