import math


def get_factors(n):
	root_n = math.sqrt(n)
	factors = {1}
	low_factors = [i for i in range(2, math.ceil(root_n) + 1) if n % i == 0]
	high_factors = map(lambda x: int(n / x), low_factors)
	factors.update(low_factors)
	factors.update(high_factors)
	return factors


amicable_numbers = set()
for i in range(2, 10000):
	num1 = sum(get_factors(i))
	num2 = sum(get_factors(num1))
	if (i == num2 and i < 10000 and num1 < 10000 and num1 != num2):
		amicable_numbers.add(num2)
		amicable_numbers.add(num1)

print(amicable_numbers)
print(sum(amicable_numbers))

