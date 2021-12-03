import numpy as np

def get_tree_count(input_, slope):
	tree_count = 0
	x = 0

	for y in np.arange(0, input_.size, slope[1]):
		if (input_[y][x] == '#'):
			tree_count += 1
		x = (x + slope[0]) % len(input_[0])

	return tree_count
	
input_ = np.array(open('input.txt').read().split('\n')[:-1])
slope = [3, 1]

# part 1
tree_count = get_tree_count(input_, slope)
#print(tree_count)

# part 2
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree_counts = []
for s in slopes:
	tree_counts.append(get_tree_count(input_, s))
print(np.prod(tree_counts))
