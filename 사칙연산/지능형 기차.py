import sys

large = list(map(int, sys.stdin.readline().strip().split()))[1]

last = large

for i in range(9):
  
  secondList = list(map(int, sys.stdin.readline().strip().split()))

  second = last  - secondList[0] + secondList[1]

  if large < second:
    large = second

  last = second
    
print(large)