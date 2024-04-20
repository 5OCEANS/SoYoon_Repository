# 런타임 에러

# import sys

# num1, num2 = sys.stdin.readline().strip().split()

# result = ''

# maxNum = max(num1, num2)

# minNum = min(num1, num2)

# result += maxNum[:len(maxNum) - len(minNum)]
# maxNum = maxNum[len(maxNum) - len(minNum):]

# for i in range(len(minNum)):
#   result += str(int(maxNum[i]) + int(minNum[i]))

# print(result)


# 성공

import sys

num1, num2 = sys.stdin.readline().split()

num1Len, num2Len = len(num1), len(num2)

if num1Len > num2Len:
  num2 = '0' * (num1Len - num2Len) + num2
else:
  num1 = '0' * (num2Len - num1Len) + num1

result = ''

for i in range(len(num1)):
  result += str(int(num1[i]) + int(num2[i]))

print(result)