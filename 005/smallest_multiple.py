def smallest_multiple(n_factors):
	factors = list(range(1, n_factors + 1))
	is_multiple = False
	val = 0
	while not bool(is_multiple):
		remainders = map(lambda x: (val + n_factors) % x, factors)
		is_multiple = all(x == 0 for x in remainders)
		val += n_factors
	return val
	
print(smallest_multiple(20))
