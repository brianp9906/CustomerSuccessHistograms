## binStats takes a csv reader object as input and outputs an array of data and ##
## an dictionary of statistical information useful for generating normal distributions ##
import statistics

def binStats(reader):
	# Initialize variables to contain datapoints from .csv and resulting statistical variables

	averageCol = 7
	binCount = 20
	averageValues = []
	stats = {}

	for idx, row in enumerate(reader):
		# Trim off top empty and header row and remove all null datapoints
		if idx == 2:
			title = row[2]
		if idx > 1 and row[averageCol] != 'No Data':
			item = row[averageCol]
			# If data is in thousands, trim off "K" and multiply value by 1000
			if "K" in item:
				item = item.replace("K", "")
				averageValues.append(float(item)*1000)
			else:
				averageValues.append(float(item))
			# Append all values of the "average" column to the averageValues array


	# Using the now populated averageValues, fill the statistics dictionary with the required values
	stats['mean'] = statistics.mean(averageValues)
	stats['median'] = statistics.median(averageValues)
	stats['mode'] = statistics.mode(averageValues)
	stats['stdev'] = statistics.pstdev(averageValues)
	stats['variance'] = statistics.variance(averageValues)
	stats['max'] = max(averageValues)
	stats['min'] = min(averageValues)
	stats['binSize'] = (stats['mean'] - stats['min']) / (binCount / 2)

	return [averageValues, stats, title]