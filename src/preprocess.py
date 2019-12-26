# python 3.6
# code to clean and process
# CSV data
# supported functions include
import re


# PFF
def clean(dataset, source):
	"""
	sanitizes a given dataset by removing erroneous
	or corrupted data
	:param dataset: array of pandas.DataFrame objects
	:return: None
	"""

	if source is 'PFF':
		for df in dataset:
			# remove NaN values
			df.dropna(inplace=True)

			# only consider qb's with 100 attempts
			df.drop(df[df.Att < 100].index, inplace=True)

			# remove extra carets from player name
			df.Player = [remove_carets(p) for p in df.Player]
	elif source is 'FO':
		for df in dataset:
			df.drop(columns=['Rk', 'Rk.1', 'Rk.2', 'Rk.3'], inplace=True)
	elif source is 'ELO':
		for df in dataset:
			df.drop(df[(df.season < 2010) | (df.season >= 2019)].index, inplace=True)
			df.fillna({'playoff': 'x'}, inplace=True)
	return dataset


def remove_carets(player_name):
	return re.sub('[*+]', '', player_name)
