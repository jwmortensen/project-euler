def gcd(a: Int, b: Int): Int = if (a == 0) b else gcd(b % a, a)
def lcm(a: Int, b: Int): Int = (a * b) / gcd(a,b)
println((1 to 19).foldLeft(20)((a,b) => lcm(a,b)))
