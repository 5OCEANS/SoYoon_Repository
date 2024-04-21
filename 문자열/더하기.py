import sys

stringList = map(int, sys.stdin.readline().strip().split(','))

sum = 0

for i in stringList:
  sum += i

print(sum)