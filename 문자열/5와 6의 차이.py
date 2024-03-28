import sys

A, B = sys.stdin.readline().strip().split()

smallA = A.replace('6', '5')
smallB = B.replace('6', '5')

smallSum = int(smallA) + int(smallB)

bigA = A.replace('5', '6')
bigB = B.replace('5', '6')

bigSum = int(bigA) + int(bigB)

print(smallSum, bigSum)