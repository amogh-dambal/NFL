# python 3.6
# code to clean and process
# CSV data
# supported functions
import re


def clean(dataset):
	"""
	sanitizes a given dataset by removing erroneous
	or corrupted data
	:param dataset: array of pandas.DataFrame objects
	:return: None
	"""
	for df in dataset:
		# remove NaN values
		df.dropna(inplace=True)

		# only consider qb's with 100 attempts
		df.drop(df[df.Att < 100].index, inplace=True)

		# remove extra carets from player name
		df.Player = [remove_carets(p) for p in df.Player]


def remove_carets(player_name):
	return re.sub('[*+]', '', player_name)

