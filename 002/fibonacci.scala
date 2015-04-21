val fibonacci:Stream[Int] = 0 #:: fibonacci.scanLeft(1)(_+_)

val limit = 4000000
println(fibonacci.takeWhile(_ <= limit).filter(_ % 2 == 0).toList.sum)
