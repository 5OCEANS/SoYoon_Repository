import sys

while 1:
    data = sys.stdin.readline().rstrip()
    if not data:
        break
    res = 0
    a, b = data.split()
    for i in range(int(a), int(b) + 1):
        if len(set(str(i))) == len(str(i)):
            res += 1
    print(res)