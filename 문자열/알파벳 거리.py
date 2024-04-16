import sys

N = int(sys.stdin.readline())

for i in range(N):
  str1, str2 = sys.stdin.readline().split()

  print('Distances: ', end= '')
  
  for j in range(len(str1)):
    if ord(str1[j]) <= ord(str2[j]):
      print(ord(str2[j])-ord(str1[j]), end = ' ')
    else:
      print(ord(str2[j])-ord(str1[j])+26, end = ' ')
  
  print()