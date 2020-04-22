from time import time
import math


def triangles():
	n = 1
	triangle = 1
	while True:
		yield triangle
		n += 1
		triangle += n


def get_factors(n):
	vals = range(1, int((n + 2) / 2))
	factors = [x for x in vals if n % x == 0]
	factors.append(n)
	return factors


def num_factors(y):
	root_y = math.sqrt(y)
	vals = range(1, int(root_y))
	n_factors = 2 * sum(map(lambda x: y % x == 0, vals))
	if root_y % 1 == 0:
		n_factors += 1
	return n_factors


tri = triangles()

start = time()
max_factors = (1, 1)
while max_factors[1] < 500:
	val = next(tri)
	n_factors = num_factors(val)
	if n_factors > max_factors[1]:
		max_factors = (val, n_factors)
		print(max_factors)
print("%s seconds elapsed" % round(time() - start))
print(max_factors)

