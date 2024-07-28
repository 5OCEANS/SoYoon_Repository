import sys

t = int(sys.stdin.readline()) 

for i in range(t):
  n = int(sys.stdin.readline())
  d = [0] * (n+1)
  
  if n == 0:
    print(1)
  elif n == 1:
    print(1)
  elif n == 2:
    print(2)
  elif n == 3:
    print(4)

  else:
    d[0] = 1
    d[1] = 1
    d[2] = 2
    d[3] = 4

    for j in range(4, n+1):
      d[j] = d[j-1] + d[j-2] + d[j-3] + d[j-4]
  
    print(d[n])