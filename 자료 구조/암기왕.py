import sys

t = int(sys.stdin.readline())

for i in range(t):
  n = int(sys.stdin.readline())
  num1Set = set(map(int, sys.stdin.readline().strip().split()))
  m = int(sys.stdin.readline())
  num2Slist = list(map(int, sys.stdin.readline().strip().split()))
  for num in num2Slist:
    if num in num1Set:
      print(1)
    else:
      print(0)