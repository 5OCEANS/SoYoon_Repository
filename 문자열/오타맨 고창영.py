import sys

T = int(sys.stdin.readline())

for i in range(T):
  index, string = sys.stdin.readline().strip().split()

  string = string[:int(index)-1] + string[int(index):]

  print(string)