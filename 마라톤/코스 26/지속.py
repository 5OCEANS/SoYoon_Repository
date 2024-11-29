import sys, math

num = int(sys.stdin.readline())
count = 0

while True:
  if num < 10:
    print(count)
    break
  stringNum = list(map(int, str(num)))
  num = math.prod(stringNum)
  count += 1