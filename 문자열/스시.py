import sys

N = int(sys.stdin.readline())

cnt = 0

for i in range(N):
  string = sys.stdin.readline().strip()
  cnt += len(string)


print(cnt)