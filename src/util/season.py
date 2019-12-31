# python 3.6
# utility class to store player information
# and simplify computation


class Season:
	# assign to default values
	# check for these when using
	name = ""
	pos = ""
	team = ""
	age = 0
	year = 0

	def __init__(self, data=None, name="", pos="", team="", age=-1, yr=-1):
		if data is None:
			self.name = name
			self.pos = pos
			self.team = team
			self.age = age
			self.year = yr
		else:
			if len(data) != 5:
				raise ValueError("list parameter has incorrect number of arguments - expected 5")
			else:
				self.name = data[0]
				self.team = data[1]
				self.age = int(data[2])
				self.pos = data[3]
				self.yr = int(data[4])

	def __str__(self):
		return \
			f"{self.name}, {self.pos}, {self.year}\n" \
			f"age: {self.age}, team: {self.team}\n"

	def __repr__(self):
		return \
			f"name: {self.name}\n" \
			f"pos: {self.pos}\n" \
			f"team: {self.team}\n" \
			f"age: {self.age}\n" \
			f"year: {self.year}\n"

	def __eq__(self, other):
		return isinstance(other, type(self)) and \
			(self.name, self.year) == (other.name, other.year)

	def __hash__(self):
		return hash((self.name, self.year))
