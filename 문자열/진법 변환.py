#  런타임 에러

# import sys

# N, B = sys.stdin.readline().strip().split()

# num = 0

# for i in range(len(N)):
#   str = N[len(N)-i-1]
#   if ord(str) >= 65 and ord(str) >= 90:
#     str = ord(str) - 55
  
#   num += int(str) * pow(int(B), i)

# print(num)


N, B = input().split()
ary = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = N[::-1]

result = 0
for i, n in enumerate(N): # 순서가 있는 자료형을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴
  result += (int(B)**i) * (ary.index(n))
print(result)