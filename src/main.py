# python 3.6
# main script to initialize and
# run the project

from parser import parse
from preprocess import clean


def main():
	pff_tuples = clean(parse(directory="../data/pff/"), 'PFF')
	fo_tuples = clean(parse(directory="../data/fo/"), 'FO')


if __name__ == '__main__':
	main()
