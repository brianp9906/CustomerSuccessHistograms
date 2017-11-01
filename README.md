# CustomerSuccessHistograms
Python script that generates a histogram based on a LogicMonitor report of Customer Success metrics

This script utilizes a number of modules:
  csv to simplify the reading of LogicMonitor .csv reports
  statistics to discern important statistical information for generating a normal distribution
  plotly is important to render histograms
  Tkinter allows users to select a .csv file manually
 
The user is prompted to open a LogicMonitor .csv file.  The script reads the file and parses it (currently) for the "Average"
column.  This data is used to produce a dictionary of statistical information which is used to determine histogram binsize,
information necessary for rendering a normal distribution, and bin frequency information.

