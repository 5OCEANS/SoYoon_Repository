import sys

numlist = sys.stdin.readline().strip()

if int(numlist[-2:])==10:
  A = int(numlist[0:-2])
  B = int(numlist[-2:])
  print(A+B)
else:
  A = int(numlist[0:-1])
  B = int(numlist[-1])
  print(A+B)