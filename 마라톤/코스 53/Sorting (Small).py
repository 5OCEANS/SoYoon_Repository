import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
  N = int(sys.stdin.readline().strip())
  nList = list(map(int, sys.stdin.readline().strip().split()))
  oddEvenList = list()
  oddlist = list()
  evenList = list()
  for num in nList:
    if num % 2 == 0:
      oddEvenList.append(0)
      evenList.append(num)
    else:
      oddEvenList.append(1)
      oddlist.append(num)
  evenList.sort(reverse=True)
  oddlist.sort()
  print('Case #%d: ' %(i+1), end='')
  for num in oddEvenList:
    if num == 0:
      print(evenList.pop(0), end=' ')
    else:
      print(oddlist.pop(0), end=' ')
  print()