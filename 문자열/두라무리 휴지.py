import sys

N = int(sys.stdin.readline())

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()

string1List = sorted(list(string1))
string2List = sorted(list(string2))

if string1List != string2List:
  print('NO')
else:
  if string1[0] != string2[0] or string1[-1] != string2[-1]:
    print('NO')
  else:
    if string1.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '') != string2.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', ''):
      print('NO')
    else:
      print('YES')