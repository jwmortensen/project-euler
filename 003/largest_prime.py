def prime_factors(n):
	factors = list()
	i = 2
	while i <= n:
		while n % i == 0:
			n /= i
			factors.append(i)
		i += 1
	return factors
	
val = 600851475143

print(prime_factors(val))
