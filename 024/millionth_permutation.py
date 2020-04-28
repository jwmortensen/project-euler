import itertools
import math


s = "0123456789"

# cheating way
perms = itertools.permutations(s)
print(next(itertools.islice(perms, 999999, 1000000)))

# by hand
digits = list(s)
perm = ""
rem = 999999
div = 9
while len(digits) > 0:
	idx, rem = divmod(rem, math.factorial(div))
	perm += digits.pop(idx)
	div -= 1
print(perm)

