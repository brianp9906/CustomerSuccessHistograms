# This function takes an array of buckets and an array of data as input
# and counts the number of datapoints in each bucket to produce y-axis data for a histogram

def frequencySort(binArray, dataArray):
	# Initialize variables to hold the length of the binArray and the max of the binArray
	binLength = len(binArray)
	binMax = max(binArray)
	# Initialize frequency information to be returned
	frequencyArray = []
	for i in range(0,binLength):
		frequencyArray.append(0)

	for item in dataArray:
		if item >= binMax:
			frequencyArray[binLength - 1] += 1
		else:
			for idx, thing in enumerate(binArray):
				# Put items from dataArray into 
				if item >= thing and item < binArray[idx + 1]:
					frequencyArray[idx] += 1

	return frequencyArray