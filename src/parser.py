# python 3.6
# take data from CSV and build data frames
# and player objects
# complete setup of all data
# and prepare data for pre processing
# basic sanitizing

import pandas as pd
import os
from glob import iglob


# read from all files in specified directory
# with specified extension
# and generate one dataframe for each year
def parse(directory="../data/**", extension=".csv"):
	path = directory + "**"
	files = [
		f for f in iglob(pathname=path, recursive=True)
		if os.path.isfile(f) and f.endswith(extension)
	]

	# each year has a dataframe
	dfs = []
	for file in files:
		df = pd.read_csv(file)
		dfs.append(df)

	return dfs



