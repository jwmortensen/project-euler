fibs = 1 : 2 : zipWith (+) fibs (tail fibs)
main = print (sum [i | i <- takeWhile (< 4000000) fibs, even i])
