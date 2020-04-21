from functools import reduce

# what are our constraints?
# c > b >= a
# a + b = 1000 - c
# a^2 + b^2 = c^2

def pyth_trip():
	sum_vals = 1000
	c_vals = range(997, 0, -1)
	for c in c_vals:
		for b in range(1, sum_vals - c):
			a = sum_vals - (b + c)
			if a * a + b * b == c * c:
				return (a, b, c)

print(reduce(lambda x, y: x * y, pyth_trip()))
	
