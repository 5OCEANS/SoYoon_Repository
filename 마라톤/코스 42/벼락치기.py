import sys

N = int(sys.stdin.readline())
if N <= 28:
  for i in range(1, 8):
    if N <= sum(range(1, i + 1)):
      print(i)
      exit(0)

else:
  print((N - 29) // 7 + 8)