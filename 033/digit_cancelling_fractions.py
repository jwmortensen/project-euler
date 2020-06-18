from numpy import prod
from euler import gcd


nums = list()
dens = list()

for i in range(1, 10):
	for j in range(1, 10):
		for k in range(i, 10):
			for l in range(1, 10):
				a = 10 * i + j
				b = 10 * k + l
				frac = a / b				
				if (
					i != k and j != l and (
					(frac == i / k and j == l) or
					(frac == i / l and j == k) or
					(frac == j / k and i == l) or
					(frac == j / l and i == k)
					)):
					#print("{}{}/{}{}".format(i, j, k, l))
					nums.append(a)
					dens.append(b)

num = prod(nums)
den = prod(dens)
print(den / gcd(num, den))
