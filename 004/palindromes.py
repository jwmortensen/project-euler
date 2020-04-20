def palindromes():
	vals = range(999, 100, -1)
	prods = [
		x * y for x in vals for y in vals
		if x * y == int(str(x * y)[::-1])
	]
	return prods
	
print(max(palindromes()))
