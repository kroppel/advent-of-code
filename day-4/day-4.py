import numpy as np
import re

def is_valid_passport(passport):
	necessary_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	for field in necessary_fields:
		if not passport.has_key(field):
			return False
	return True

input_ = open('input.txt').read().split('\n\n')
p_count = 0

for block in input_:
	block = re.split(' |\n', block)
	passport = {}
	for field in block:
		# Last block contains empty field due to ending on \n
		if (field != ''):
			field = field.split(':')
			passport.update({field[0]:field[1]})
	if is_valid_passport(passport):
		p_count += 1

print(p_count)
