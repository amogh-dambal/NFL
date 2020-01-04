# python 3.6
# utility code to help
# with graphing things

from matplotlib import pyplot as plt


def graph(x, y, params=None):
	"""

	:param x: x-axis data
	:param y: y-axis data
	:param x_label: the label for the x axis
	:param y_label: the label for the y axis
	:param params: dictionary for other graphing settings
	:return: whether plot was successful
	"""
	plt.scatter(x, y, color='darkorange' if params is None else params['color'])
	plt.xlabel('' if params is None else params['xlabel'])
	plt.ylabel('' if params is None else params['ylabel'])

	if params is not None:
		plt.title(f"{params['title']}")

	plt.show()


def extract(x_label, y_label, year, seasons=None, database=None):
	"""

	:param x_label: label for the x-axis
	:param y_label: label for the y-axis
	:param seasons: list of Season objects to pull from
	:param database: list of dataframes to pull from
	:param year: year from which data will be extracted
	:return: tuple: (X axis data points, Y axis data points)
	"""
	if seasons is not None:
		if database is not None:
			raise ValueError("Must specify exactly one of seasons and database")
		else:
			# extract graph data from array of season objects
			x = []
			y = []
			data = [s for s in seasons if s.year == year]
			print(data)
			for szn in data:
				x.append(float(szn.labeled_stats[x_label]))
				y.append(float(szn.labeled_stats[y_label]))

			return x, y
	elif database is not None:
		# extract graph data from array of pandas.DataFrame
		pass
	else:
		raise ValueError("Must specify exactly one of seasons and database")
