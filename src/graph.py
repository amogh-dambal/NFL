# python 3.6
# utility code to help
# with graphing things

from matplotlib import pyplot as plt


def graph(x, y, n=[], params=None):
	"""
	Function to graph the provided data with specified parameters
	using the pyplot library
	:param x: x-axis data
	:param y: y-axis data
	:param params: dictionary for other graphing settings. supported parameters:
		xlabel - the label for the x-axis
		ylabel - the label for the y-axis
		title - the title for the plot
		color - the color for the markers
		marker - the style of the marker
	:return: whether plot was successful
	"""
	# TODO: write code to label markers
	plt.scatter(
		x, y,
		marker='x' if params is None else params['marker'],
		color='darkorange' if params is None else params['color']
	)
	plt.xlabel('' if params is None else params['xlabel'])
	plt.ylabel('' if params is None else params['ylabel'])

	if params is not None:
		plt.title(f"{params['title']}")

	if len(n) > 0:
		for px, py, pname in zip(x, y, n):
			plt.annotate(s=pname, xy=(px, py))

	plt.grid(True, color='black', linewidth=.1)
	ax = plt.axes()

	ax.spines['left'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')
	ax.spines['left'].set_smart_bounds(True)
	ax.spines['bottom'].set_smart_bounds(True)
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	plt.show()


def extract(x_label, y_label, year, seasons=None, database=None, names=False):
	"""

	:param x_label: label for the x-axis
	:param y_label: label for the y-axis
	:param seasons: list of Season objects to pull from
	:param database: list of dataframes to pull from
	:param year: year from which data will be extracted
	:param names: whether to include the names of the players or not
	:return: tuple: (X axis data points, Y axis data points)
	"""
	if seasons is not None:
		if database is not None:
			raise ValueError("Must specify exactly one of seasons and database")
		else:
			# extract graph data from array of season objects
			x = []
			y = []
			n = []
			data = [s for s in seasons if s.year == year]
			print(data)
			for szn in data:
				x.append(float(szn.labeled_stats[x_label]))
				y.append(float(szn.labeled_stats[y_label]))
				if names:
					n.append(szn.name)

			return x, y, n
	elif database is not None:
		# extract graph data from array of pandas.DataFrame
		pass
	else:
		raise ValueError("Must specify exactly one of seasons and database")
