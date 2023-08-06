#!/usr/bin/python

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
import shutil
import math
import json
#import os
from string import Template
from importlib.resources import files
from pathlib import Path
from ebib.indexer import index, read_pdf, text_to_doi, checksum, import_metadata, empty_metadata
from ebib.utils import load_info, save_info, run_command

@click.command()
def webpage():
	ebib_info = load_info()

	public_path = Path('public')
	public_path.mkdir(exist_ok = True)
	pdf_path = public_path.joinpath('pdf')
	pdf_path.mkdir(exist_ok = True)
	assets_path = files('ebib.assets')
	shutil.copy2(assets_path.joinpath('index.html'), public_path)
	with open(assets_path.joinpath('index.html'), 'r') as fi, open(public_path.joinpath('index.html'), 'w') as fo:
		t = Template(fi.read())
		fo.write(t.substitute(title = ebib_info['name']))
	shutil.copy2(assets_path.joinpath('index.js'), public_path)
	shutil.copy2(assets_path.joinpath('english-stemmer.js'), public_path)

	data = {
		'pdfs': {},
		'idf': {},
		'avgdl': 0
	}
	for pdf in ebib_info['pdfs']:
		shutil.copy2(pdf + '.pdf', pdf_path.joinpath(pdf + '.pdf'))
		data['pdfs'][pdf] = ebib_info['pdfs'][pdf]
		data['pdfs'][pdf]['index'], data['pdfs'][pdf]['length'] = index(read_pdf(pdf + '.pdf'))
		for term in data['pdfs'][pdf]['index']:
			if term in data['idf']:
				data['idf'][term] += 1
			else:
				data['idf'][term] = 1
		data['avgdl'] += data['pdfs'][pdf]['length']
	if len(ebib_info['pdfs']) > 0:
		data['idf'] = {t: math.log((len(ebib_info['pdfs']) - n + 0.5)/(n + 0.5) + 1) for t,n in data['idf'].items()}
		data['avgdl'] = data['avgdl'] / len(ebib_info['pdfs'])
	with open(public_path.joinpath('data.json'), 'w') as f:
		json.dump(data, f)

@click.command()
@click.argument('filepath', type = click.Path(exists = True))
@click.option('--doi', '-d', help = 'DOI of the imported document')
@click.option('--force', is_flag = True, help = 'Force when detecting checksum coincidence')
@click.option('--nodoi', is_flag = True, help = 'Add PDF file without DOI. (Metadata will be empty)')
def add(filepath, doi, force, nodoi):
	ebib_info = load_info()
	csum = checksum(filepath)

	if not nodoi:
		full_text = read_pdf(filepath)
		if doi is None:
			doi = text_to_doi(full_text)
			if not doi:
				print("ERROR: Could not extract DOI from PDF file")
				exit(1)
		metadata = import_metadata(doi)

		filename = metadata['authors'][0].split(',')[0] + str(metadata['year'])
		if filename in ebib_info['pdfs']:
			if csum == ebib_info['pdfs'][filename]['checksum']:
				print('WARN: "{}" and "{}" have the same checksum.'.format(filepath, filename + '.pdf'))
				if not force:
					print('      Are you trying to add the same document two times?')
					exit(1)
			ebib_info['pdfs'][filename + 'a'] = ebib_info['pdfs'].pop(filename)
			shutil.move(filename + '.pdf', filename + 'a.pdf')
		i = 97
		while (filename + chr(i)) in ebib_info['pdfs']:
			i += 1
		filename += chr(i) if i > 97 else ''
	else:
		metadata = empty_metadata
		filename = Path(filepath).stem
		if filename in ebib_info['pdfs']:
			print('ERROR: a file called "{}" already exists.'.format(filename + '.pdf'))
			exit(1)

		for pdf in ebib_info['pdfs']:
			if ebib_info['pdfs'][pdf]['checksum'] == csum:
				print('WARN: "{}" and "{}" have the same checksum.'.format(filepath, pdf + '.pdf'))
				if not force:
					print('      Are you trying to add the same document two times?')
					exit(1)

	shutil.copy2(filepath, filename + '.pdf')
	metadata['checksum'] = csum
	metadata['tags'] = []
	ebib_info['pdfs'][filename] = metadata
	save_info(ebib_info)

	run_command(['git', 'add', '.'])
	run_command(['git', 'commit', '-m', 'Added ' + filename + '.pdf'])

@click.command()
@click.argument('filename')
@click.argument('tags', nargs = -1)
def add_tag(filename, tags):
	ebib_info = load_info()

	if filename not in ebib_info['pdfs']:
		print('ERROR: no file named "{}" is known'.format(filename))
		exit(1)

	for tag in tags:
		if tag in ebib_info['pdfs'][filename]['tags']:
			print('WARN: tag "{}" already added to {}'.format(tag, filename))
		else:
			ebib_info['pdfs'][filename]['tags'].append(tag)

	save_info(ebib_info)
	run_command(['git', 'add', '.'])
	mtags = ' '.join(map(lambda x: '"' + x + '"', tags))
	run_command(['git', 'commit', '-m', 'Added tag' + ('s' if len(tags) > 0 else '') + ' ' + mtags + ' to ' + filename + '.pdf'])
	print(['git', 'commit', '-m', 'Added tag' + ('s' if len(tags) > 0 else '') + ' ' + mtags + ' to ' + filename + '.pdf'])

@click.command()
@click.argument('name')
@click.option('--gitlab', is_flag = True, help = 'Include gitlab ci')
def init(name, gitlab):
	info_ebib = Path('info.ebib')
	if info_ebib.is_file():
		print('ERROR: Repository already Initialized')
		exit(1)
	run_command(['git', 'init'])
	ebib_info = {'name': name, 'pdfs': {}}
	save_info(ebib_info)
	with open('.gitignore', 'w') as f:
		f.write('public')
	if gitlab:
		shutil.copy2(files('ebib.assets').joinpath('.gitlab-ci.yml'), '.')
		run_command(['git', 'add', '.gitlab-ci.yml'])
	run_command(['git', 'add', 'info.ebib'])
	run_command(['git', 'add', '.gitignore'])
	run_command(['git', 'commit', '-m', 'Initialized ' + name])

@click.group(help='CLI tool for bibliography manager integrated with git.')
def cli():
	pass

cli.add_command(webpage)
cli.add_command(add_tag)
cli.add_command(add)
cli.add_command(init)

if __name__ == '__main__':
	cli()
