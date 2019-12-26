# python 3.6
# code to clean and process
# CSV data
# supported functions include
import re


def clean(dataset, source):
	"""
	sanitizes a given dataset by removing erroneous
	or corrupted data
	:param dataset: array of pandas.DataFrame objects
	:param source: the website where the data comes from as a string
	:return: None
	"""

	if source is 'PFF':
		for df in dataset:
			# remove NaN values
			df.dropna(inplace=True)

			# only consider qb's with 100 attempts
			df.drop(df[df.Att < 100].index, inplace=True)

			# remove extra carets from player name
			# and only use last name
			# to allow us to merge with FO data
			df.Player = [standardize(p) for p in df.Player]
	elif source is 'FO':
		for df in dataset:
			df.drop(columns=['Rk'], inplace=True)
			df.Player = [p[2:] for p in df.Player]
	elif source is 'ELO':
		for df in dataset:
			df.drop(df[(df.season < 2010) | (df.season >= 2019)].index, inplace=True)
			df.fillna({'playoff': 'x'}, inplace=True)
	return dataset


# remove extraneous characters
# and return the last name
def standardize(player_name):
	player_name = re.sub('[*+]', '', player_name)
	return player_name.split(sep=' ')[1]

