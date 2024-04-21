import sys

n = int(sys.stdin.readline())

for i in range(n):
  string = sys.stdin.readline().strip().lower()

  backwards = string[::-1]

  if string == backwards:
    print('Yes')
  else:
    print('No')