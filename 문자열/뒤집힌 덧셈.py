import sys

X, Y = sys.stdin.readline().strip().split()

X = X[::-1]
Y = Y[::-1]

result = int(str(int(X) + int(Y))[::-1])

print(result)