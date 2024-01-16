import sys
m = int(sys.stdin.readline())
s = []

for __ in range(m):
  instruc = sys.stdin.readline().split()
  if 'add' == instruc[0]:
    if int(instruc[1]) not in s:
      s.append(int(instruc[1]))
  elif 'remove' == instruc[0]:
    if int(instruc[1]) in s:
      s.remove(int(instruc[1]))
  elif 'check' == instruc[0]:
    if int(instruc[1]) in s:
      print(1)
    else:
      print(0)
  elif 'toggle' == instruc[0]:
    if int(instruc[1]) in s:
      s.remove(int(instruc[1]))
    else:
      s.append(int(instruc[1]))
  elif 'all' == instruc[0]:
    s = [num for num in range(1, 21, 1)]
  elif 'empty' == instruc[0]:
    s= []
  
  