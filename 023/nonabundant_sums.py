import math
import time


def get_divisors(n):
    root_n = math.sqrt(n)
    divisors = {1}
    low_divisors = [i for i in range(2, math.ceil(root_n) + 1) if n % i == 0]
    high_divisors = map(lambda x: int(n / x), low_divisors)
    divisors.update(low_divisors)
    divisors.update(high_divisors)
    return divisors


n_max = 28123
abundant_numbers = set()
for n in range(12, n_max):
    div = get_divisors(n)
    if sum(div) > n:
        abundant_numbers.add(n)

start = time.time()
abundant_sums = set()
while abundant_numbers:
    i = abundant_numbers.pop()
    abundant_sums.update(map(lambda x: x + i, abundant_numbers))
    abundant_sums.add(2 * i)

print("%s second elapsed" % round(time.time() - start, 2))

abundant_sums = set(filter(lambda x: x < n_max, abundant_sums))

nonabundant_sums = filter(lambda x: x not in abundant_sums, range(1, n_max))

print(sum(nonabundant_sums))

