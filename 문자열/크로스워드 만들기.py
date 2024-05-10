import sys

A, B = sys.stdin.readline().strip().split()
index = 30
Aindex = 30

for i in range(len(A)):
  if A[i] in list(B):
    index = B.index(A[i])
    Aindex = i
    break

for i in range(len(B)):
  if i == index:
    print(A)
    continue
  for j in range(len(A)):
    if j == Aindex:
      print(B[i], end='')
    else:
      print('.', end='')
  
  print()