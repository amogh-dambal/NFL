# python 3.6
# main script to initialize and
# run the project

from parser import parse
from preprocess import clean, merge, build_seasons

import pprint


def main():
	# generate database
	pff_tuples = clean(parse(directory="../data/pff/"), 'PFF')
	fo_tuples = clean(parse(directory="../data/fo/"), 'FO')

	database = []
	for pff, fo in zip(pff_tuples, fo_tuples):
		joined, yr = merge(pff, fo)
		database.append((joined, yr))

	all_seasons = build_seasons(database=database)

	pp = pprint.PrettyPrinter(indent=3)
	pp.pprint(all_seasons)


if __name__ == '__main__':
	main()
