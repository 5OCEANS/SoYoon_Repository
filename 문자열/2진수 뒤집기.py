import sys

print(int(str(bin(int(sys.stdin.readline())))[2:][::-1], 2))