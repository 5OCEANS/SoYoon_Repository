import sys

S = sys.stdin.readline().strip()

newS = ''

K = sys.stdin.readline().strip()

for i in range(len(S)):
  if S[i].isalpha():
    newS += S[i]

if K in newS:
  print(1)
else:
  print(0)