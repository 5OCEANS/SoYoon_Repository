import sys

n = int(sys.stdin.readline())

for _ in range(n):
  string = sys.stdin.readline().strip()

  print(string) if string[-1] == '.' else print(string+'.')