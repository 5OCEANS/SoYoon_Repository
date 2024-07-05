import sys

A, B = map(int, sys.stdin.readline().strip().split())

aRow = A // 4 if A % 4 != 0 else A // 4 -1
aCol = A % 4 if A % 4 != 0 else 4

bRow = B // 4 if B % 4 != 0 else B // 4 - 1
bCol = B % 4 if B % 4 != 0 else 4

res = abs(aRow - bRow) + abs(aCol - bCol)

print(res)