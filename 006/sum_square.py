def square(x):
		return x * x


def sum_squares_diff(max_range):
	vals = range(1, max_range + 1)
	sum_squares = sum(map(square, vals))
	square_sum = square(sum(vals))
	return square_sum - sum_squares
	
print(sum_squares_diff(100))
