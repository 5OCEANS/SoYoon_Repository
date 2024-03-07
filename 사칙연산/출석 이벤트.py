import sys

N = int(sys.stdin.readline())
P = int(sys.stdin.readline())

if N >= 5 and N < 10:
  print(int(max(P-500, 0)))
elif N >= 10 and N < 15:
  print(int(max(min(P-500, P*0.9), 0)))
elif N >= 15 and N < 20:
  print(int(max(min(P-500, P*0.9, P-2000), 0)))
elif N >= 20:
  print(int(max(min(P-2000, P*0.75), 0)))
elif N < 5:
  print(P)