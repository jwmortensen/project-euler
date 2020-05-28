upper_limit = 6 * pow(9, 5)

powers = list(map(lambda x: pow(x, 5), range(10)))

keep = []
for i in range(2, upper_limit):
	val = i
	s = 0
	while val > 0:
		s += powers[val % 10]
		val = val // 10
	if s == i:
		keep.append(i)
print(keep)
print(sum(keep))
