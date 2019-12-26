# python 3.6
# utility class to store player information
# and simplify computation
import numpy as np


class Player:
	_name = ""
	_pos = ""
	_team = ""
	_age = 0

	def __init__(self, data=None, name="", pos="", team="", age=-1):
		if data is None:
			self._name = name
			self._pos = pos
			self._team = team
			self._age = age
		else:
			if len(data) != 4:
				raise ValueError("list parameter has incorrect number of arguments - expected 4")
			else:
				self._name = data[0]
				self._team = data[1]
				self._age = int(data[2])
				self._pos = data[3]

	def __str__(self):
		return \
			f"name: {self._name}\n" \
			f"pos: {self._pos}\n" \
			f"team: {self._team}\n" \
			f"age: {self._age}\n"

	def __repr__(self):
		return \
			f"name: {self._name}\n" \
			f"pos: {self._pos}\n" \
			f"team: {self._team}\n" \
			f"age: {self._age}\n"

	def __eq__(self, other):
		return isinstance(other, type(self)) and \
			self._name == other._name

	def __hash__(self):
		return hash(self._name)
