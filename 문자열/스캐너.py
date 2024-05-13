import sys

R, C, ZR, ZC = map(int, sys.stdin.readline().strip().split())

result = []

for i in range(R):
  string = list(sys.stdin.readline().strip())
  for j in range(ZR):
    result.append([tmpstr*ZC for tmpstr in string]) 

for i in range(R*ZR):
  print(''.join(result[i]))