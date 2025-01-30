import sys

B1 = sys.stdin.readline().strip()
B2 = sys.stdin.readline().strip()

ans = bin(int(B1, 2) * int(B2, 2))[2:]

print(ans)