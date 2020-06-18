# can't have zero
# what's the largest number of valid digits for the multiples?
# it seems like they have to be either 1 and 4 so that 1+4+4 = 9 or 2 and 3
# (10*100=1000 -> 2+3+4)

import itertools

def is_pandigital(a, b, c):
	in_digits = list(str(a)+str(b)+str(c))
	equal_length = len(in_digits) == len(digits)
	return equal_length and set(in_digits) == set(digits)

digits = list(map(lambda x: str(x), [1,2,3,4,5,6,7,8,9]))
vals = set()
perms = itertools.permutations(digits, 5)
	
for p in perms:
	a = int(p[0])
	b = int(''.join(p[1:5]))
	c = a * b
	if is_pandigital(a, b, c):
		vals.add(c)
	a = int(''.join(p[0:2]))
	b = int(''.join(p[2:6]))
	c = a*b
	if is_pandigital(a, b, c):
		print('{a}*{b}={c}'.format(a=a,b=b,c=c))
		vals.add(c)
		

print(sum(vals))
