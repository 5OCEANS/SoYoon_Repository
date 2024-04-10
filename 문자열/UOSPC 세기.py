import sys

n = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

ucnt = string.count('u')
ocnt = string.count('o')
scnt = string.count('s')
pcnt = string.count('p')
ccnt = string.count('c')

print(min(ucnt, ocnt, scnt, pcnt, ccnt))