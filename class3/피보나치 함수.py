
# 0 - 1 0
# 1 - 0 1
# 2 - 1 1
# 3 - 1 2
# 4 - 2 3
# 5 - 3 5
# 6 - 5 8

import sys 

fibonacciList = [[0, 1] for __ in range(41)]
fibonacciList[0] = [1, 0]
fibonacciList[1] = [0, 1]

for i in range(2, 41, 1):
  fibonacciList[i][0] = fibonacciList[i-2][0] + fibonacciList[i-1][0]
  fibonacciList[i][1] = fibonacciList[i-2][1] + fibonacciList[i-1][1]

t = int(sys.stdin.readline().strip())

for i in range(t):
  n = int(sys.stdin.readline().strip())
  print(fibonacciList[n][0], fibonacciList[n][1])