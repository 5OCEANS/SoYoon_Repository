import sys

T = int(sys.stdin.readline())

for i in range(T):
  N = int(sys.stdin.readline())
  XList = list(map(int, sys.stdin.readline().strip().split()))

  for j in range(1, N):
    XList[j] = max(XList[j], XList[j] + XList[j-1])
  
  print(max(XList))