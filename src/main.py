# python 3.6
# main script to initialize and
# run the project

from parser import parse
from preprocess import clean, merge, build_seasons
from graph import extract, graph


def main():
	# generate database
	pff_tuples = clean(parse(directory="../data/pff/"), 'PFF')
	fo_tuples = clean(parse(directory="../data/fo/"), 'FO')

	database = []
	for pff, fo in zip(pff_tuples, fo_tuples):
		joined, yr = merge(pff, fo)
		database.append((joined, yr))

	# build individual season records
	all_seasons = build_seasons(database=database)

	# plot QB efficiency in 2018
	x_label = 'DYAR'
	y_label = 'DVOA'

	X, Y = extract(x_label=x_label, y_label=y_label, seasons=all_seasons)

	graph(x=X, y=Y, x_label=x_label, y_label=y_label)


if __name__ == '__main__':
	main()
