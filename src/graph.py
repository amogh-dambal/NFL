# python 3.6
# utility code to help
# with graphing things

from matplotlib import pyplot as plt


def graph(x, y, x_label, y_label):
	"""

	:param x: x-axis data
	:param y: y-axis data
	:param x_label: the label for the x axis
	:param y_label: the label for the y axis
	:return: whether plot was successful
	"""
	plt.scatter(x, y, color='darkorange')
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.xticks(())
	plt.yticks(())
	plt.title("A Measure of QB Efficiency, 2018")
	plt.show()


def extract(x_label, y_label, seasons=None, database=None):
	"""

	:param x_label: label for the x-axis
	:param y_label: label for the y-axis
	:param seasons: list of Season objects to pull from
	:param database: list of dataframes to pull from
	:return: tuple: (X axis data points, Y axis data points)
	"""
	if seasons is not None:
		if database is not None:
			raise ValueError("Must specify exactly one of seasons and database")
		else:
			# extract graph data from array of season objects
			x = []
			y = []
			for szn in seasons:
				x.append(szn.labeled_stats[x_label])
				y.append(szn.labeled_stats[y_label])

			return x, y
	elif database is not None:
		# extract graph data from array of pandas.DataFrame
		pass
	else:
		raise ValueError("Must specify exactly one of seasons and database")
