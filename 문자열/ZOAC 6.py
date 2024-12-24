import sys

ans = 0
N = int(sys.stdin.readline())
for _ in range(N):
  string = sys.stdin.readline().strip()
  if '01' in string or 'OI' in string:
    ans += 1
print(ans)