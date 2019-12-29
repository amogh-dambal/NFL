# python 3.6
# main script to initialize and
# run the project

from parser import parse
from preprocess import clean


def main():
	pff_tuples = parse(directory="../data/pff/")
	fo_tuples = parse(directory="../data/fo/")

	clean(pff_tuples, 'PFF')
	clean(fo_tuples, 'FO')

	flush(dataset=pff_tuples, source='PFF', path='../data/cleaned/', extension='.csv')
	flush(dataset=fo_tuples, source='FO', path='../data/cleaned/', extension='.csv')

	print('cleaned and flushed data.')


if __name__ == '__main__':
	main()
