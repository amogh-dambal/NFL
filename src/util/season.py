# python 3.6
# utility class to store player information
# and simplify computation
import copy


class Season:
	def __init__(self, data=None, name="", pos="", team="", age=-1, yr=-1, column_names=None):
		if data is None:
			self.name = name
			self.pos = pos
			self.team = team
			self.age = age
			self.year = yr
		else:
			# data is a pandas.Series object
			# load player information
			player_info = data.iloc[:4]
			self.name = player_info[0]
			self.team = player_info[1]
			self.age = player_info[2]
			self.pos = player_info[3]
			self.year = yr

			# load player stats
			player_stats = data.iloc[4:]
			self.raw_stats = copy.deepcopy(player_stats)

			# assign to labeled stats
			self.labeled_stats = {}
			if column_names is None:
				print("No labels provided - labeled stats will not be recorded")
			else:
				for label, stat in zip(column_names, player_stats):
					if label not in self.labeled_stats:
						self.labeled_stats[label] = stat

	def get_fv(self):
		"""
		returns the feature vector for this season
		to be used in clustering algorithms
		:return: list of floating point numbers that are selected features of a season
		"""
		return copy.deepcopy(self.raw_stats)

	def __str__(self):
		return f"{self.name}, {self.pos}/{self.team}, {self.year}\n" \
			f"stats: {self.labeled_stats}\n"

	def __repr__(self):
		return f"{self.name}, {self.pos}/{self.team}, {self.year}\n" \
			f"stats: {self.labeled_stats}\n"

	def __eq__(self, other):
		return isinstance(other, type(self)) and \
			(self.name, self.year) == (other.name, other.year)

	def __hash__(self):
		return hash((self.name, self.year))
