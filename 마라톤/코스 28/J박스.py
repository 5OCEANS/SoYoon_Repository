import sys

t = int(sys.stdin.readline())
for i in range(t):
  size = int(sys.stdin.readline())
  for j in range(size):
    if j == 0 or j == (size-1):
      print('#'*(size))
    else:
      print('#'+'J'*(size-2)+'#')
  print()