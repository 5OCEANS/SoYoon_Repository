import sys

N, H, W = map(int, sys.stdin.readline().strip().split())
stringList = []

alphaList = ['?' for _ in range(N)]

for i in range(H):
  string = sys.stdin.readline().strip()
  
  for j in range(len(string)):
    if string[j].isalpha():
      alphaList[j//W] = string[j]

print(''.join(alphaList))