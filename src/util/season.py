# python 3.6
# utility class to store player information
# and simplify computation


class Season:
	_name = ""
	_pos = ""
	_team = ""
	_age = 0
	_year = 0

	def __init__(self, data=None, name="", pos="", team="", age=-1, yr=-1):
		if data is None:
			self._name = name
			self._pos = pos
			self._team = team
			self._age = age
			self._year = yr
		else:
			if len(data) != 5:
				raise ValueError("list parameter has incorrect number of arguments - expected 5")
			else:
				self._name = data[0]
				self._team = data[1]
				self._age = int(data[2])
				self._pos = data[3]
				self._yr = int(data[4])

	def __str__(self):
		return \
			f"{self._name}, {self._pos}, {self._year}\n" \
			f"age: {self._age}, team: {self._team}\n"

	def __repr__(self):
		return \
			f"name: {self._name}\n" \
			f"pos: {self._pos}\n" \
			f"team: {self._team}\n" \
			f"age: {self._age}\n" \
			f"year: {self._year}\n"

	def __eq__(self, other):
		return isinstance(other, type(self)) and \
			(self._name, self._year) == (other._name, other._year)

	def __hash__(self):
		return hash((self._name, self._year))
