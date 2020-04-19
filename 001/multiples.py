import timeit

def pe1_brute_force(max_val):
	total = 0
	for val in range(max_val):
		if val % 3 == 0 or val % 5 == 0:
			total += val
	return total

print(pe1_brute_force(1000))


def pe1(max_val):
	return sum([val for val in range(max_val) if val % 3 == 0 or val % 5 == 0])

start_time = time.time()
print(pe1(1000))
end_time = time.time()
print("%s seconds elapsed" % round(end_time - start_time, 6))
