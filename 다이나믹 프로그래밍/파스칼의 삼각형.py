import sys

n, k = map(int, sys.stdin.readline().strip().split())

pascal = [[1], [1, 1]]

if n <= 2:
  print(pascal[n-1][k-1])

for i in range(2, n):
  list = [1]
  for j in range(1, i):
    num = pascal[i-1][j-1] + pascal[i-1][j]
    list.append(num)
  list.append(1)
  pascal.append(list)

  if i == n-1:
    print(list[k-1])
    break