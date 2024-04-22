# 틀렸습니다. 

# import sys

# T = int(sys.stdin.readline())

# for i in range(T):
#   A, n = map(int, sys.stdin.readline().split())
#   ans = ''

#   while True:
#     if A == 0:
#       break

#     x = A % n
#     ans += str(x)
#     A //= n

  
#   if ans == ans[::-1]:
#     print(1)
#   else:
#     print(0)


# 성공

t = int(input())

for i in range(t):
  a, n = map(int, input().split())

  res = ""

  while a > 0:
    res += str(hex(a % n)[2:])
    a //= n
  if res == res[::-1]:
    print(1)
  else:
    print(0)