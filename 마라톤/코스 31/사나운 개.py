import sys

A, B, C, D = map(int, sys.stdin.readline().strip().split())
delivery = list(map(int, input().split()))

for i in delivery:
  dog = 0
  if 0 < i % (A + B) <= A: #
    dog += 1
  if 0 < i % (C + D) <= C:
    dog += 1
      
  print(dog)