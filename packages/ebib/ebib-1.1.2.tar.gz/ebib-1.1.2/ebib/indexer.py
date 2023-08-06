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

import click
import requests
import json
import fitz
import re
import hashlib

from ebib import Lexer

from typing import Dict, List, Tuple

month_transform = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

type_converter = {
	'book': 'book',
	'book-chapter': 'inbook',
	'book-part': 'inbook',
	'book-section': 'inbook',
	'book-series': 'incollection',
	'book-set': 'incollection',
	'book-track': 'inbook',
	'dataset': 'misc',
	'dissertation': 'phdthesis',
	'edited-book': 'book',
	'journal-article': 'article',
	'journal-issue': 'misc',
	'journal-volume': 'article',
	'monograph': 'monograph',
	'other': 'misc',
	'peer-review': 'article',
	'posted-content': 'misc',
	'proceedings-article': 'inproceedings',
	'proceedings': 'inproceedings',
	'proceedings-series': 'inproceedings',
	'reference-book': 'book',
	'report': 'report',
	'report-series': 'inproceedings',
	'standard-series': 'incollection',
	'standard': 'techreport',
}  # type: Dict[str, str]

#transformations = {
#	'publisher': [('publisher', lambda x: x)],
#	'issue': [('number', lambda x: x)],
#	'container-title': [('journal', lambda x: x)],
#	'published-print': [
#		('year', lambda x: x['date-parts'][0][0]),
#		('month', lambda x: month_transform[x['date-parts'][0][1]-1]),
#	],
#	'published-online': [
#		('year', lambda x: x['date-parts'][0][0]),
#		('month', lambda x: month_transform[x['date-parts'][0][1]-1]),
#	],
#	'issued': [
#		('year', lambda x: x['date-parts'][0][0]),
#		('month', lambda x: month_transform[x['date-parts'][0][1]-1]),
#	],
#	'DOI': [
#		('doi', lambda x: x),
#		('url', lambda x: 'https://doi.org/' + x),
#	],
#	'URL': [('url', lambda x: x)],
#	'page': [('pages', lambda x: x)],
#	'title': [('title', lambda x: x)],
#	'volume': [('volume', lambda x: x)],
#	'author': [('author', transform_author_list)],
#	'ISSN': [('isnn', lambda x: x[0])],
#	'type': [('type', lambda x: type_converter[x])]
#}
#
#ignored_keys = [
#	'indexed', 'reference-count', 'license', 'content-domain',
#	'short-container-title', 'created', 'source',
#	'is-referenced-by-count', 'prefix', 'member',
#	'reference', 'original-title', 'language', 'link',
#	'deposited', 'score', 'resource', 'subtitle', 'short-title',
#	'references-count', 'journal-issue', 'alternative-id',
#	'relation', 'subject', 'container-title-short', 'published',
#
#]

empty_metadata = {
	'publisher': '',
	'number': '',
	'journal': '',
	'doi': '',
	'url': '',
	'pages': '',
	'title': '',
	'volume': '',
	'authors': '',
	'issn': '',
	'type': 'article',
	'year': '',
	'month': '',
}

def import_metadata(doi: str) -> Dict[str, str]:
	r = requests.get('https://doi.org/' + doi, headers = {'accept': 'application/json'})

	if r.status_code == 404:
		print('ERROR: Invalid or unsupported DOI')
		exit(1)
	if r.status_code != 200:
		print('ERROR: DOI service unaviable')
		exit(1)

	d_metadata = json.loads(r.text)

	def value_or_none(a):
		return d_metadata[a] if a in d_metadata else ''

	metadata = {
		'publisher': value_or_none('publisher'),
		'number': value_or_none('issue'),
		'journal': value_or_none('conatiner-title'),
		'doi': value_or_none('DOI'),
		'url': d_metadata['URL'] if 'URL' in d_metadata else 'https://doi.org/' + value_or_none('DOI'),
		'pages': value_or_none('page'),
		'title': value_or_none('title'),
		'volume': value_or_none('volume'),
		'authors': list(map(lambda x: '{x[family]}, {x[given]}'.format(x=x), d_metadata['author'])),
		'issn': d_metadata['ISSN'][0] if 'ISSN' in d_metadata else '',
		'type': type_converter[d_metadata['type']],
		'year': d_metadata['issued']['date-parts'][0][0],
		'month': month_transform[d_metadata['issued']['date-parts'][0][1]-1],
	}
	print(metadata)

#	for k, v in d_metadata.items():
#		if k in transformations:
#			for ind, fn in transformations[k]:
#				metadata[ind] = fn(v)
#		elif k not in ignored_keys:
#			print('ERROR: Unknown message key "{}" => {}.'.format(k, v))
#			exit(1)
	return metadata

def read_pdf(filepath: str) -> str:
	pdf = fitz.open(filepath)
	return '\n'.join([page.get_text() for page in pdf])

def clean_doi(text: str) -> str:
	text = re.sub(r'%2F', '/', text)
	# For pdfs
	text = re.sub(r'\)>', ' ', text)
	text = re.sub(r'\)/S/URI', ' ', text)
	text = re.sub(r'(/abstract)', '', text)
	text = re.sub(r'\)$', '', text)
	return text

def text_to_doi(text: str) -> str:
	forbidden_doi_characters = r'"\s%$^\'<>@,;:#?&'
	# Sometimes it is in the javascript defined
	var_doi = re.compile(
		r'doi(.org)?'
		r'\s*(=|:|/|\()\s*'
		r'("|\')?'
		r'(?P<doi>[^{fc}]+)'
		r'("|\'|\))?'
		.format(
			fc=forbidden_doi_characters
		), re.I
	)
	for regex in [var_doi]:
		for m in regex.finditer(text):
			doi = m.group('doi')
			return clean_doi(doi)

def index(text: str) -> Dict[str, int]:
	idx = {}
	len = 0
	for token in Lexer(text):
		if token in idx:
			idx[token] += 1
		else:
			idx[token] = 1
		len += 1
	return idx, len

def checksum(filepath: str) -> str:
	with open(filepath, 'rb') as f:
		return hashlib.md5(f.read()).hexdigest()
