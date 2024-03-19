import sys

N = int(sys.stdin.readline())

for i in range(N):
  string = str(sys.stdin.readline().strip())

  print(string[0].upper()+string[1:])