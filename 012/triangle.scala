import scala.math.sqrt

lazy val ts: Stream[Int] = 0 #:: ts.zipWithIndex.map(t => t._1 + t._2 + 1)

def numFactors(x: Int): Int = {
  Range(1, Int.MaxValue)
    .takeWhile(n => n * n <= x)
    .foldLeft(0)((s, n) => if (x % n == 0) s + 2 else s)
}

println(ts.find(numFactors(_) > 500).get)


