

object Multiples {
  
  def getMultiples(n: Int): List[Int] = {
    val seq = List.range(1,n)
    seq.filter(x => x % 3 == 0 | x % 5 == 0)
  }
  
  def sum(xs: List[Int]): Int = {
    xs.reduceLeft {(x,y) => x + y}
  }

  def main(args: Array[String]) {
    if (args.length > 0) {
      val multiples = getMultiples(args(0).toInt)
      println(sum(multiples))
    }
    else 
      println("Please specify an integer.")
  } 
}
