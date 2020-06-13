"""
the way to count ways to make change is to count the number of ways to make
change with the largest coin and the number of ways without it. So for 5 we can
make change as
5
2 2 1
2 1 1 1
1 1 1 1 1

for 10 we have:
10
5 5
5 2 2 1
5 2 1 1 1
5 1 1 1 1 1
2 2 2 2 2
2 2 2 2 1 1
2 2 2 1 1 1 1
2 2 1 1 1 1 1 1
2 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
"""


def ways_to_make_change(amount):
	def count(coins, idx, amount):
		if idx >= 0:
			if amount - coins[idx] == 0:
				return 1
			elif amount - coins[idx] > 0:
				return sum(
					map(lambda i: count(coins, i, amount - coins[idx]), range(0, idx + 1)))
			elif amount - coins[idx] < 0:
				return 0
		else:
			return 0

	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	num = 0
	for i in range(len(coins)):
		num += count(coins, i, amount)
	return (num)


print(ways_to_make_change(200))

