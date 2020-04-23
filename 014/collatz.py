from time import time


def collatz(x):
	while x > 1:
		yield x
		if x % 2 == 0:
			x /= 2
		else:
			x = 3 * x + 1
	yield x


def get_chain_length(x):
	n = 0
	for item in collatz(x):
		remaining_length = known_lengths.get(item, None)
		if remaining_length is None:
			n += 1
		else:
			n += remaining_length
			break
	return n


# using this dictionary decreases speed from ~30 seconds to 3
known_lengths = {13: 10}
start_time = time()
max_length = (13, 10)
for x in range(1, 1000000):
	n = get_chain_length(x)
	known_lengths[x] = n
	if n > max_length[1]:
		max_length = (x, n)
print(max_length)
print("%s seconds elapsed" % round(time() - start_time))

