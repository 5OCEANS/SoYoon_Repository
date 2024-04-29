import sys

N = int(sys.stdin.readline())

string = list(sys.stdin.readline().strip())
lowerstr = ['r', 'o', 'y', 'g', 'b', 'i', 'v']
upperstr = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']

lower = []
upper = []

aSign = 0
dSign = 0

for i in string:
  if i.isupper():
    upper.append(i)
  elif i.islower():
    lower.append(i)

if all(str in lower for str in lowerstr):
  aSign = 1
if all(str in upper for str in upperstr):
  dSign = 1

if aSign == 1 and dSign == 1:
  print('YeS')
elif aSign == 1 and dSign == 0:
  print('yes')
elif aSign == 0 and dSign == 1:
  print('YES')
else:
  print('NO!')