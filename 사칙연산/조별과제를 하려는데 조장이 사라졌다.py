import sys

L = int(sys.stdin.readline().strip())

res = L // 5 if L% 5 == 0 else L//5+1

print(res)