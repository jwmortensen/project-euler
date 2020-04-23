def choose(n: Int, k: Int) = (BigInt(k+1) to BigInt(n)).product / (BigInt(2) to BigInt(k)).product
println(choose(40, 20))
