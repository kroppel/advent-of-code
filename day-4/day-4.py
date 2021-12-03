import numpy as np
import re

# due to python only supporting match (switch) statements with version 3.10,
# I used nested conditionals
def is_valid_field_value(field, value):
		if (field == 'byr'):	
			if value.isnumeric():
				return(1920 <= int(value) <= 2002)
			else: 
				return False
		if (field == 'iyr'):	
			if value.isnumeric():
				return(2010 <= int(value) <= 2020)
			else: 
				return False
		if (field == 'eyr'): 
			if value.isnumeric():
				return(2020 <= int(value) <= 2030)
			else: 
				return False
		if (field == 'hgt'): 
			if (value[-2:] == 'cm'):
				if value[:-2].isnumeric():
					return(150 <= int(value[:-2]) <= 193)
				else: 
					return False
			if (value[-2:] == 'in'):
				if value[:-2].isnumeric():
					return(59 <= int(value[:-2]) <= 76)
				else: 
					return False
			else:
				return False
		if (field == 'hcl'): 
			return (value[0] == '#' and len(value[1:]) == 6 and 
			((x.isnumeric() or x in ['a', 'b', 'c', 'd', 'e', 'f']) for x in value[1:]))
		if (field == 'ecl'):
			return (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
		if (field == 'pid'):
			return (value.isnumeric() and len(value) == 9)

def is_valid_passport(passport):
	necessary_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	for field in necessary_fields:
		if not field in passport:
			return False
		# part 2
		else: 
			if not is_valid_field_value(field, passport[field]):
				print(field + ': ' + passport[field])
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
