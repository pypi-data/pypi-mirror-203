# Copyright (C) 2023 Ernesto Lanchares <elancha98@gmail.com>
# 
# This file is part of ebib.
# 
# ebib is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# ebib is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with ebib. If not, see <https://www.gnu.org/licenses/>.

from typing import Callable
from ebib import EnglishStemmer

stemmer = EnglishStemmer()

class Lexer:
	def __init__(self, text: str):
		self.text = text
	def trim_left(self):
		while self.text and self.text[0].isspace():
			self.text = self.text[1:]

	def chop(self, i: int) -> str:
		assert(len(self.text) > i)
		token = self.text[0:i]
		self.text = self.text[i:]
		return token

	def chop_while(self, fn: Callable[[chr], bool]) -> str:
		i = 0
		while self.text and fn(self.text[i]):
			i += 1
		return self.chop(i)

	def __next__(self) -> str:
		self.trim_left()
		if not self.text:
			raise StopIteration

		if self.text[0].isnumeric():
			return self.chop_while(lambda x: x.isnumeric())
		if self.text[0].isalpha():
			term = self.chop_while(lambda x: x.isalnum()).lower()
			return stemmer.stemWord(term)

		return self.chop(1)

	def __iter__(self):
		return self
