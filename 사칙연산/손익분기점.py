import sys

A, B, C = map(int, sys.stdin.readline().strip().split())

if B>=C: # A + B * n == C * n 일 때 수입과 비용이 같아짐. -> B >= C 일 경우는 손익분기점이 나타나지 않게 됨.
  print(-1)
else:
  print(int(A/(C-B)+1))