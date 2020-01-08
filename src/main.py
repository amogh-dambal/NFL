# python 3.6
# main script to initialize and
# run the project

from parser import parse
from preprocess import clean, merge, build_seasons
from graph import extract, graph


def setup(directory):
	# generate database

	pff_tuples = clean(parse(directory=directory+"pff/"), 'PFF')
	fo_tuples = clean(parse(directory=directory+"fo/"), 'FO')

	database = []
	for pff, fo in zip(pff_tuples, fo_tuples):
		joined, yr = merge(pff, fo)
		database.append((joined, yr))

	# build individual season records
	all_seasons = build_seasons(database=database)

	return all_seasons


def main():

	seasons = setup("../data/")


if __name__ == '__main__':
	main()
