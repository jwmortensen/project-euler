val fibonacci:Stream[BigInt] = BigInt(0) #:: fibonacci.scanLeft(BigInt(1))(_+_)

def sum(xs: List[BigInt]): BigInt =  xs.reduceLeft {(x,y) => x + y}

val limit = 4000000
val fibs = fibonacci.takeWhile(_ <= limit).filter(x => x % 2 == 0).toList
println(sum(fibs))
