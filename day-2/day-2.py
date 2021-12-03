import numpy as np
import re

input = np.array(open('input.txt').read().split('\n')[:-1])
pw_count = 0

for line in input:
	policy, password = line.split(':')

	# represent policies as list [lower_bound, upper_bound, letter]
	policy = re.split('-| ', policy)
	password = np.array(list(password.strip(' ')))
	
	# second half
	# boolean expressions that evaluate to true if given position
	# holds the policy letter
	first_position = password[(int(policy[0])-1)] == policy[2]
	second_position = password[(int(policy[1])-1)] == policy[2]

	# if XOR on both boolean expressions is true, increment counter
	if (first_position and not second_position) or (not first_position 
	    and second_position):
		pw_count += 1
		
	"""
	# first half
	# if password complies with the policy, increment counter
	l_count = len(password[password == policy[2]])
	if (int(policy[0]) <= l_count <= int(policy[1])):
		pw_count += 1
	"""
	
print(pw_count)
	
