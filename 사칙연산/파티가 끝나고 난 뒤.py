import sys

L, P = map(int, sys.stdin.readline().strip().split())
numList = sys.stdin.readline().strip().split()

people = L*P

for num in numList:
  print(int(num)-people, end=" ")