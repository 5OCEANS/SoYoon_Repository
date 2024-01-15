import sys
n = int(sys.stdin.readline())
stack = []
start = 1
res = []

for i in range(n):
  end = int(sys.stdin.readline())
  while start <= end:
    stack.append(start)
    res.append('+')
    start += 1
  if stack[-1] == end:
    stack.pop()
    res.append('-')
  else:
    print("NO")
    break
else:
  for i in res:
    print(i)