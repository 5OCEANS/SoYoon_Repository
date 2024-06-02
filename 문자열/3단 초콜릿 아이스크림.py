import sys

T = int(sys.stdin.readline())

for i in range(T):
  string = sys.stdin.readline().strip()

  oneThird = string[0:len(string)//3 if len(string)%3 == 0 else len(string)//3+1]

  if string == oneThird + oneThird[::-1] + oneThird:
    print(1)
    continue
  elif string == oneThird + oneThird[::-1][1:] + oneThird:
    print(1)
    continue
  elif string == oneThird + oneThird[::-1] + oneThird[1:]:
    print(1)
    continue
  elif string == oneThird + oneThird[::-1][1:] + oneThird[1:]:
    print(1)
    continue
  else:
    print(0)