# python 3.6
# code to clean and process
# CSV data
# supported functions include
import re


def clean(dataset, source):
	"""
	sanitizes a given dataset by removing erroneous
	or corrupted data
	:param dataset: array of tuples (pandas.DataFrame, int)
	:param source: the website where the data comes from as a string
	:return: None
	"""

	if source is 'PFF':
		for df, yr in dataset:
			# remove NaN values
			df.dropna(inplace=True)

			# only consider qb's with 100 attempts
			df.drop(df[df.Att < 100].index, inplace=True)

			# remove extra carets from player name
			# and only use last name
			# to allow us to merge with FO data
			df.Player = [standardize(p) for p in df.Player]
	elif source is 'FO':
		for df, yr in dataset:
			df.drop(columns=['Rk'], inplace=True)
			df.Player = [p[2:] for p in df.Player]
	elif source is 'ELO':
		for df, yr in dataset:
			df.drop(df[(df.season < 2010) | (df.season >= 2019)].index, inplace=True)
			df.fillna({'playoff': 'x'}, inplace=True)
	return dataset


def flush(dataset, source, path, extension):
	"""
	write a dataset to file system 
	:param dataset: array of tuples (DataFrame, int) to write
	:param source: website data originates from
	:param path: directory to write to
	:param extension: type of file
	:return: none
	"""
	for df, yr in dataset:
		filename = path + f"{source}_" + str(yr) + extension
		df.to_csv(filename)


# remove extraneous characters
# and return the last name
def standardize(player_name):
	player_name = re.sub('[*+]', '', player_name)
	return player_name.split(sep=' ')[1]

