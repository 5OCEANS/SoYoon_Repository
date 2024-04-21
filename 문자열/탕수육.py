# 짝수의 경우는 2칸씩 증가시킨 값만 말하면 된다.
# 홀수는 예를 들면 카카오페이의 경우 처음에는 2칸씩(카O오O이) 증가시킨 값을 출력하고, 그 뒤에 (O카O페O) 부분을 더해서 출력해주면 된다.

import sys

T = int(sys.stdin.readline())

for i in range(T):
  string = sys.stdin.readline().strip()

  first = ''
  second = ''

  if len(string) % 2 == 0:
    first = string[0::2]
    second = string[1::2]
  else:
    first = string[0::2] + string[1::2]
    second = string[1::2] + string[0::2]
  
  print(first)
  print(second)