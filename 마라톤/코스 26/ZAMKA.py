import sys

L = int(sys.stdin.readline())
D = int(sys.stdin.readline())
X = int(sys.stdin.readline())

for i in range(L, D+1):
  if (sum(map(int, list(str(i))))) == X:
    print(i)
    break
for i in range(D, L-1, -1):
  if (sum(map(int, list(str(i))))) == X:
    print(i)
    break