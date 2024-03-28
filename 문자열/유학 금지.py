import sys

string = sys.stdin.readline().strip()
newString = ''

for i in string:
  if i not in 'CAMBRIDGE':
    newString += i

print(newString)