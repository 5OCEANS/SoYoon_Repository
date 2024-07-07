import sys

index = 1

while True:
  n0 = int(sys.stdin.readline().strip())
  if n0 == 0:
    break

  n4 = 0

  if n0 % 2 == 0: # even
    n4 = n0 // 2
    print('%d. even %d' %(index, n4))
  else: # odd
    n4 = (n0 - 1) // 2
    print('%d. odd %d' %(index, n4))
  
  index += 1