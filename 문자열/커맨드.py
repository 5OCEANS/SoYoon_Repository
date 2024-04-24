import sys

T = int(sys.stdin.readline())

for i in range(T):
  N = sys.stdin.readline().strip()

  if len(N) != 7:
    print(0)
    continue

  first = N[0]
  second = N[2]

  if first == second:
    print(0)
    continue

  expectation = first* 2 + second * 2 + first + second * 2

  if expectation != N:
    print(0)
    continue
  else:
    print(1)