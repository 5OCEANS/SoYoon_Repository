import sys

N, K = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().strip().split(',')))

for i in range(K):
  B = []
  for j in range(len(A)-1):
    B.append(A[j+1] - A[j])
  
  A = B

for i in range(len(A)):
  if i == len(A) - 1:
    print(A[i])
  else:
    print(A[i], end = ',')


# print 쉽게 하는 방법
print(",".join(map(str, A)))