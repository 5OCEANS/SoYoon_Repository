strCnt = int(input())

strList = [str(input()) for __ in range(strCnt)]

strList = list(set(strList))
strList.sort()
strLenList = strList.sort(key=lambda x: len(x))

for i in strList:
    print(i)