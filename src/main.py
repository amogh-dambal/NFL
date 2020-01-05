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

	# plot QB efficiency in 2018
	x_label = 'DVOA'
	y_label = 'DYAR'

	year_ = 2017
	x_, y_ = extract(x_label=x_label, y_label=y_label, year=year_, seasons=seasons)
	params = {
		'title': f'QB Efficiency, {year_}',
		'color': 'red',
		'xlabel': 'DVOA',
		'ylabel': 'DYAR',
		'season': '2018'
	}

	graph(x=x_, y=y_, params=params)


if __name__ == '__main__':
	main()
