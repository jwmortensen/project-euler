def square(n: Int) = n * n
val ints = 1 to 100
val diff = square(ints.sum) - ints.map(square).sum
println(diff)

