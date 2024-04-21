import sys

T = int(sys.stdin.readline())

for i in range(T):
  string = sys.stdin.readline().strip()

  list = [0] * 26

  for i in string:
    if i.isalpha():
      list[ord(i)-97] += 1
  
  if list.count(max(list)) != 1:
    print('?')
  else:
    print(chr(list.index(max(list))+97))