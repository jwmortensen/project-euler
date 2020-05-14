from euler import prime_sieve



def quad_form(n, a, b):
	return n**2 + a * n + b

max_n = 1000
max_a = 1000
max_b = 1001
primes = list(prime_sieve(quad_form(max_n, max_a, max_b)))
b_vals = list(prime_sieve(max_b))

best = [0, 0, 0]
for b in b_vals:
	print(b)
	a_vals = filter(lambda x: x < 1000, map(lambda p: p - b - 1, primes))
	for a in a_vals:
		n = 0
		while quad_form(n, a, b) in primes:
			n += 1
		if n > best[2]:
			best = [a, b, n]

			

