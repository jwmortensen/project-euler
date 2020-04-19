import timeit

def multiples_brute_force(max_val):
	total = 0
	for val in range(max_val):
		if val % 3 == 0 or val % 5 == 0:
			total += val
	return total

print(multiples_brute_force(1000))


def multiples(max_val):
	return sum([val for val in range(max_val) if val % 3 == 0 or val % 5 == 0])


print(multiples(1000))

print("brute force time:")
print(timeit.timeit("multiples_brute_force(1000)", number=10000, globals=globals()))
print("list comprehension time:")
print(timeit.timeit("multiples(1000)", number=10000, globals=globals()))
