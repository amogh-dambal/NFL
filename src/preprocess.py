# python 3.6
# code to clean and process
# CSV data
# supported functions include
import re

from util.season import Season


def clean(dataset, source):
	"""
	sanitizes a given dataset by removing erroneous
	or corrupted data
	:param dataset: array of tuples (pandas.DataFrame, int)
	:param source: the website where the data comes from as a string
	:return: sanitized array of tuples: (pandas.DataFrame, int)
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

			# rename column that represents sack yardage
			df.rename({'Yds.1':'SkYds'}, axis='columns', inplace=True)
	elif source is 'FO':
		for df, yr in dataset:
			df.dropna(inplace=True)
			df.drop(columns=df.filter(like='Rk'), inplace=True)
			df.Player = [p[2:] for p in df.Player]
	elif source is 'ELO':
		for df, yr in dataset:
			df.dropna(inplace=True)
			df.drop(df[(df.season < 2010) | (df.season >= 2019)].index, inplace=True)
			df.fillna({'playoff': 'x'}, inplace=True)
	return dataset


def merge(f1, f2, index='Player'):
	"""
	combines two pandas.DataFrame objects into one
	on the specified index ('Player') and sanitizes it
	:param f1: tuple (pandas.DataFrame, year) object to call merge
	:param f2: tuple (pandas.DataFrame, year) object to merge
	:param index: string to merge on
	:return: sanitized pandas.DataFrame object
	"""

	if int(f1[1]) != int(f2[1]):
		raise ValueError("Merging datasets of different years!")

	year = int(f1[1])
	pff = f1[0]
	fo = f2[0]

	joined = pff.join(other=fo.set_index(index), on=index, rsuffix='fo')
	joined.dropna(inplace=True)
	joined.drop(columns=[c for c in joined.columns if c.endswith('fo')] + ['Team', 'Yards'], inplace=True)

	return joined, year


def build_seasons(database):
	"""
	generate a list of
	:param database: full
	:return: list of Season objects for all player seasons from 2010-2018
	"""
	all_seasons = []
	for df, yr in database:
		for row in df.iterrows():
			all_seasons.append(Season(data=row[1], yr=yr, column_names=df.columns[4:]))
	return all_seasons


# remove extraneous characters
# and return the last name
def standardize(player_name):
	player_name = re.sub('[*+]', '', player_name)
	return player_name.split(sep=' ')[1]

