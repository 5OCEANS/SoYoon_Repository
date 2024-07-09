import sys

N = int(sys.stdin.readline().strip())
ans = 0

for i in range(N):
  student, apple = map(int, sys.stdin.readline().strip().split())

  ans += (apple % student)

print(ans)