import sys

n = int(sys.stdin.readline())
nList = [0] * (n+1)

if n == 0:
  print(0)
elif n == 1:
  print(1)
else:
  nList[1] = 1

  for i in range(2, n+1):
    nList[i] =(nList[i-1] + nList[i-2])%1000000007

  print(nList[n])