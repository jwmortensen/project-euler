def prime_sieve(limit):
	prime = [True] * limit
	prime[0] = prime[1] = False
	
	for i, is_prime in enumerate(prime):
		if is_prime:
			yield i
			for n in range(i * i, limit, i):
				prime[n] = False

print(sum(prime_sieve(2000000)))
