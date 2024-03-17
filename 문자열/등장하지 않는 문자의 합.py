import sys

alphabet = {'A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

T = int(sys.stdin.readline().strip())

for i in range(T):
  s = set(sys.stdin.readline().strip())
  a = alphabet - s
  sum = 0

  for j in a:
    sum += ord(j)
  
  print(sum)