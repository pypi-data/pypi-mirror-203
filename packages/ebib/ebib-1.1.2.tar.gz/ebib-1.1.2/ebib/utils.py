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

import json
import subprocess

def run_command(args):
	p = subprocess.run(args)
	if p.returncode != 0:
		print('ERROR: Failed to execute command "' + ' '.join(args) + '".')
		exit(1)

def load_info():
	try:
		with open('info.ebib', 'r') as f:
			return json.load(f)
	except FileNotFoundError:
		print('ERROR: ebib repository not initialized')
		exit(1)

def save_info(info):
	with open('info.ebib', 'w') as f:
		json.dump(info, f)
