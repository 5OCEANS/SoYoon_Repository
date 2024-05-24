import sys

S = sys.stdin.readline().strip()

ans = ''
ans += S[0]
cnt = 0

for i in range(1, len(S)):
  if int(S[i-1]) == int(S[i]) - 1:
    ans += S[i]
  else:
    if len(ans) == 3:
      cnt += 1
    ans = ''
    ans += S[i]

if len(ans) == 3:
  cnt += 1

print(cnt)