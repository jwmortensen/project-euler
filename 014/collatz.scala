import scala.annotation.tailrec

@tailrec def collatz(n: Long, length: Int): Int = {
  if (n == 1) length
  else if (n % 2 == 0) collatz(n / 2, length + 1)
  else collatz(3 * n + 1, length + 1)
}

println((1 until 1000000).map(x => (x, collatz(x, 1)))
  .reduceLeft((a,b) => if (a._2 > b._2) a else b)._1)

