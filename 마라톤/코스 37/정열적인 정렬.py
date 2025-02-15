import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().strip().split()))

numList.sort()

print(*numList)