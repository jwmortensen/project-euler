a = range(2, 101)
b = range(2, 101)

print(len(set([pow(x, y) for x in a for y in b])))
