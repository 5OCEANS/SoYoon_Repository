import sys

N = int(sys.stdin.readline().strip())
card = 1

if N <= 10:
  print(1)
    
else:
  while N >= card:
    card = str(card)
    card += '1'
    card = int(card)
  
  print(len(str(card//10)))