import sys

haveToFind = sys.stdin.readline().strip()

N = int(sys.stdin.readline())
cnt = 0

for i in range(N):
  string = sys.stdin.readline().strip()
  string = string * 2

  if haveToFind in string:
    cnt += 1

print(cnt)
  
