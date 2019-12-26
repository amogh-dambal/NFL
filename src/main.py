# python 3.6
# main script to initialize and
# run the project

from parser import parse


def main():
	pff_tuples = parse(directory="../data/pff/")
	fo_tuples = parse(directory="../data/fo/")

	# TODO: add support to keep track of the year
	# TODO: represented by the DataFrame

	print('all clear.')


if __name__ == '__main__':
	main()
