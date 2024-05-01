import sys

bin = sys.stdin.readline().strip()

oct = oct(int(bin, 2))[2:]

print(oct)