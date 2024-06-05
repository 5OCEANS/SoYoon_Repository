import sys

numList = list(sys.stdin.readline().strip())

numList.sort(reverse=True)

print(''.join(numList))