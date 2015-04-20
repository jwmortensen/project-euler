def isPalindrome(n: Int) = n.toString == n.toString.reverse

val maxPalindrome = (100 to 999)
  .flatMap(i => (i to 999).map(i * _))
  .filter(isPalindrome(_)).max
println(maxPalindrome)
