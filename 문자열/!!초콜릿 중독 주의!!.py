import sys, math

T = int(sys.stdin.readline())

for i in range(T):
  string = sys.stdin.readline().strip()
  a = 0
  n = 0
  b = 0

  result = ''

  for j in string:
    if j == '!':
      a += 1
    else:
      break
  
  n = int(string[a])
  b = len(string) - (a + 1)

  result = n

  for j in range(b):
    result = math.factorial(n)

  if result % 2 == 0:
    if a % 2 != 0:
      result = 1
  else:
    if a % 2 != 0:
      result = 0
  
  print(result)