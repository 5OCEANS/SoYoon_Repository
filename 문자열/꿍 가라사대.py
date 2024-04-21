import sys

N = int(sys.stdin.readline())

for i in range(N):
  string = sys.stdin.readline().strip()

  if string.startswith('Simon says'):
    print(string[10:])