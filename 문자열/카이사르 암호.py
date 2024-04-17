import sys

string = sys.stdin.readline().strip()
newstring = ''

for i in range(len(string)):
  if ord(string[i]) - 3 < 65:
    newstring += chr(ord(string[i])-3 + 26)
  else:
    newstring += chr(ord(string[i])-3)

print(newstring)