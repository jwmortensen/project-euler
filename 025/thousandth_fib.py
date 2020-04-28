from itertools import takewhile


def fib(n):
	a, b = 0, 1
	for _ in range(n):
		yield b
		a, b = b, a + b

fib_seq = fib(100000)
num = 0
i = 0
while len(str(num)) < 1000 and num is not None:
	num = next(fib_seq)
	i += 1
print(num)
print(i)
