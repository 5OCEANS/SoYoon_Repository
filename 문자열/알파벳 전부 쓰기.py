import sys

N = int(sys.stdin.readline())

for i in range(N):
  string = sys.stdin.readline().lower()

  list = [0] * 26

  for j in string:
    if j.isalpha():
      list[ord(j)-97] = 1
  
  if sum(list) == 26:
    print('pangram')
  else:
    print('missing', end = ' ')
    
    for k in range(list.count(0)):
      print(chr(list.index(0)+97+k), end='')
      list.remove(0)

    print()