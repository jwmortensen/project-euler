val n = 1000
val multiples = (1 to (n-1)).filter(x => x % 3 == 0 | x % 5 == 0).toList.sum
println(multiples)
