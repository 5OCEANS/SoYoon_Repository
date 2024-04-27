import sys

S = sys.stdin.readline().strip()

if 'A' in S:
  S = S.replace('B', 'A').replace('C', 'A').replace('D', 'A').replace('F', 'A')
elif 'B' in S:
  S = S.replace('C', 'B').replace('D', 'B').replace('F', 'B')
elif 'C' in S:
  S = S.replace('D', 'C').replace('F', 'C')
else:
  length = len(S)
  S = 'A' * length

print(S)