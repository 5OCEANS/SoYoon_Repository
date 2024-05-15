import sys

n = int(sys.stdin.readline())

word = sys.stdin.readline()
numtotal = 0
i = 0
while i < n:
  num = '0'
  while True:
    if word[i].isdigit():
      num += word[i]
      i += 1
    else:
      i += 1
      break
  
  numtotal += int(num)
  
print(numtotal)