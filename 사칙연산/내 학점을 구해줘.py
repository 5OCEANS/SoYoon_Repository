import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  N = int(sys.stdin.readline().strip())
  totalC = 0
  totalG = 0.0

  for j in range(N):
    C, G = sys.stdin.readline().strip().split()
    C = int(C)
    totalC += C
    G = float(G)

    totalG += (C * G)

  print('%d %0.1f' %(totalC, totalG / totalC))  