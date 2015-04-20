def isPalindrome(n: Int): Boolean = {
   val str = n.toString
   str == str.reverse
}

val l1 = 100 to 999
val maxPalindrome = l1.combinations(2)
  .map(x => x(0) * x(1))
  .filter(isPalindrome(_)).max
println(maxPalindrome)
