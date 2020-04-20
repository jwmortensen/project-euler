from itertools import takewhile


def fib(n):
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, a + b

fib_vals = takewhile(lambda x: x < 4000000, fib(100000))
print(sum([x for x in fib_vals if x % 2 == 0]))
