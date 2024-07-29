import sys

n = int(sys.stdin.readline())

nList = [0] * (n+1)
nList[0] = 1

for i in range(1, n+1):
  for j in range(n):
    nList[i] += nList[j]*nList[(i-1)-j] 

print(nList[n])