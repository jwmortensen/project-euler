def gcd(a, b):
	if a == 0:
		return b
	else:
		return gcd(b % a, a)

def lcm(a, b):
	return (a * b) / gcd(a, b)
	
def smallest_multiple(n_factors):
	multiple = 1
	for i in range(2, n_factors + 1):
		multiple = lcm(multiple, i)
	return multiple
	
print(smallest_multiple(20))
