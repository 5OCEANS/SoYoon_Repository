import sys

N = int(sys.stdin.readline().strip())

sum = 0 

for i in range(N+1):
  sum += pow(i, 3)

print(sum)