# python 3.6
# main script to initialize and
# run the project

from parser import parse
from preprocess import clean


def main():
	pff_dfs = parse(directory="../../data/pff/")
	fo_dfs = parse(directory="../../data/fo/")

	clean(pff_dfs, 'PFF')
	clean(fo_dfs, 'FO')

	print('all clear.')


if __name__ == '__main__':
	main()
