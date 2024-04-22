import sys

N = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

string1 = list(string.replace('2', ' ').split())
string2 = list(string.replace('1', ' ').split())

if string1.count('1') == N and string2.count('2') == N:
  print('Yes')
else:
  print('No')