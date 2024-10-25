import sys

H = int(sys.stdin.readline().strip())
W = int(sys.stdin.readline().strip())

smallOne = H if H <= W else W

print(int((smallOne / 2) * 100))