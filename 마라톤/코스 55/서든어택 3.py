import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))

jun = arr.pop(0)
arr.sort()

for i in arr :
  if jun > i : 
    jun += i
  else :
    print("No")
    break
else:
  print("Yes")