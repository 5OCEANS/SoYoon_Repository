import sys

string = sys.stdin.readline().strip()
count = len(string) // 10

for i in range(count):
  print(string[i*10:(i+1)*10])

if (len(string) % 10) != 0:
  print(string[(10*count):])