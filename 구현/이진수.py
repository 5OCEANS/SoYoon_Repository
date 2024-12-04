import sys

T = int(sys.stdin.readline())

for i in range(T):
  n = int(sys.stdin.readline())
  binN = list(str(bin(n)))[::-1]
  for j in range(len(binN)):
    if binN[j] == '1':
      print(j, end = ' ') 