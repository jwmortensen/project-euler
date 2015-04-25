val nums = 1 to 1000
val triple = for(b <- 2 to 1000; a <- 1 until b; c = 1000 - a - b
              if (a * a + b * b == c * c)) yield a * b * c
println(triple(0))
