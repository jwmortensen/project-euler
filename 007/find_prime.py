from time import time
import itertools


def sieve(n):
	block_size = 100
	block_start = 1
	vals = range(3, block_size, 2)
	primes = {2}
	
	while len(primes) < n:
		primes.add(vals[0])
		vals = [x for x in vals[1:] if x % vals[0] != 0]
		while len(vals) < 2:
			block_start += block_size
			new_vals = list(range(block_start, block_start + block_size, 2))
			poss_primes = filter(lambda x: all(x % y != 0 for y in primes), new_vals)
			vals.extend(poss_primes)
	return primes

# start = time()
# print(max(sieve(10001)))
# print("%s seconds elapsed" % str(round(time() - start, 2)))


# more efficient implementation after consulting the internet
def prime_sieve(limit):
	prime = [True] * limit
	prime[0] = prime[1] = False
	
	for i, is_prime in enumerate(prime):
		if is_prime:
			yield i
			for n in range(i * i, limit, i):
				prime[n] = False

start = time()
primes = prime_sieve(150000)
print(next(itertools.islice(primes, 10000, None)))
print("%s seconds elapsed" % str(round(time() - start, 2)))
