import sys

string = sys.stdin.readline().strip()
string1 = string[0:len(string)//3]
string2 = string[len(string)//3:(len(string)//3)*2]
string3 = string[(len(string)//3)*2:]

if string1 == string2:
  print(string1)
elif string1 == string3:
  print(string1)
elif string2 == string3:
  print(string2)