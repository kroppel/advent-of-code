import numpy as np
import time
import itertools

def solution0(input_):
	for num1 in input_:
		for num2 in input_:
			if ((num1 + num2) == 2020 and num1 != num2):
				print(str(num1) + ', ' + str(num2) + ', ' + str(num1 * num2))
				break
		else:
			continue
		break

def solution1(input_):
	for num1 in input_:
		remainder = 2020 - num1
		if (num1 != remainder):
			if (np.isin(input_, [remainder], True).sum() > 0):
				print(str(num1) + ', ' + str(remainder) + ', ' + str(num1*remainder))
				break

def solution2(input_):
	for (num1, num2) in itertools.product(input_, input_):
		if ((num1 + num2) == 2020 and num1 != num2):
				print(str(num1) + ', ' + str(num2) + ', ' + str(num1 * num2))
				break

input_ = np.array(open('input.txt').read().split('\n')[:-1], int)
solutions = [solution0, solution1, solution2]
exec_times = []

for i in np.arange(3):
	start_time = time.time()
	solutions[i](input_)
	exec_times.append(time.time() - start_time)

print(exec_times)
