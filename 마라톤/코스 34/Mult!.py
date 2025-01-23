import sys

n = int(sys.stdin.readline())

count = 0
while count < n:
  num = int(sys.stdin.readline())
  count += 1
  while count < n:
    num2 = int(sys.stdin.readline())
    count += 1
    if num2 % num == 0:
      print(num2)
      break