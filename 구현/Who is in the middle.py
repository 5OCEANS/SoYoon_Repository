import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
num3 = int(sys.stdin.readline())

numList = [num1, num2, num3]
numList.sort()
print(numList[1])