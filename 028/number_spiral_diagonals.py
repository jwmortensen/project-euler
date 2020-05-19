import numpy as np


def spiral_idx(center, r):
	if r == 0:
		yield (center, center)
	else:
		for i in range(-r + 1, r):
			yield (center + i, center + r)
		for i in range(r, -r, -1):
			yield (center + r, center + i)
		for i in range(r, -r, -1):
			yield (center + i, center - r)
		for i in range(-r, r + 1):
			yield (center - r, center + i)


def spiral(grid_size):
	spiral = np.zeros([grid_size, grid_size], dtype=int)
	center = grid_size // 2
	val = 1
	for r in range(grid_size - center):
		for idx in spiral_idx(center, r):
			spiral[idx[0], idx[1]] = val
			val += 1
	return spiral


sp1 = spiral(1001)
sumval = 0
for i in range(sp1.shape[0]):
	sumval += sp1[i, i]
	j = sp1.shape[0] - i - 1
	if i != j:
		sumval += sp1[i, j]
print(sumval)

