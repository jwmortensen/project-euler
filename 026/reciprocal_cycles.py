import euler

# using fermats theorem
primes = list(euler.prime_sieve(1000))

def cycle_length(d):
	cyc_len = None
	n = 0
	while cyc_len is None and n < d:
		n += 1
		if pow(10, n, d) == 1:
			cyc_len = n
	return(n)

max_cycle = 0
max_d = 0
for d in reversed(primes):
	cyc = cycle_length(d)
	if max_cycle < cyc:
		max_cycle = cyc
		max_d = d
	if max_cycle > d:
		break
print(max_d)
print(max_cycle)
