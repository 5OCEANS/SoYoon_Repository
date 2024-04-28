import sys

J, N = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(N):
  string = sys.stdin.readline().rstrip()
  score = 0

  for j in string:
    if j.isupper():
      score += 4
    elif j.islower() or j.isdigit():
      score += 2
    elif j.isspace():
      score += 1
    
  if J >= score:
    cnt += 1

print(cnt)