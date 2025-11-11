T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    prices = list(map(int, input().split()))

    max_future = 0
    profit = 0

    for p in reversed(prices):
        if p >= max_future:
            max_future = p
        else:
            profit += (max_future - p)

    print(f"#{tc} {profit}")


T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    board = [[0] * N for _ in range(N)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    r, c = 0, 0

    for num in range(1, N * N + 1):
        board[r][c] = num
        nr, nc = r + dirs[d][0], c + dirs[d][1]

        if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = r + dirs[d][0], c + dirs[d][1]

        r, c = nr, nc

    print(f"#{tc}")
    for row in board:
        print(' '.join(map(str, row)))


# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
from collections import defaultdict
T = int(input())
for tc in range(1, T + 1):
    tcNum = input()
    scoreList = list(map(int, input().split()))
    scoreDict = defaultdict(int)
    for score in scoreList:
        scoreDict[score] += 1
    manyScore = sorted(scoreDict.items(), key=(lambda x:(x[1], x[0])), reverse=True)
    print(f'#{tcNum} '+ str(manyScore[0][0]))


# 2001. 파리 퇴치
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    maxPari = 0
    nList = list()
    for n in range(1, N + 1):
        num = list(map(int, input().split()))
        nList.append(num)
    for xStart in range((N-M+1)):
        for yStart in range((N-M+1)):
            pari = 0
            for x in range(M):
                for y in range(M):
                    pari += nList[xStart + x][yStart + y]
            if pari > maxPari:
                maxPari = pari
    print(f'#{tc} '+ str(maxPari))

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            s = 0
            for x in range(M):
                s += sum(arr[i + x][j:j + M])
            max_sum = max(max_sum, s)

    print(f"#{tc} {max_sum}")


# 1926. 간단한 369게임
def trannum(n):
    nStr = str(n)
    if '3' in nStr or '6' in nStr or '9' in nStr:
        nStr = '-' * (nStr.count('3') + nStr.count('6') + nStr.count('9'))
    return nStr

N = int(input())
for num in range(1, N+1):
    print(trannum(num), end = ' ')


# 1928. Base64 Decoder
T = int(input())
for tc in range(1, T+1):
    string = input()
    bitNum = ''
    decodingString = ''
    for char in string:
        if char.isupper():
            bitNum += ('%06d' % (int(bin(ord(char) - 65)[2:])))
        elif char.islower():
            bitNum += ('%06d' % (int(bin(ord(char) - 71)[2:])))
        elif char.isdigit():
            bitNum += ('%06d' % (int(bin(ord(char) +4)[2:])))
        elif char == '+':
            bitNum += ('%06d' % (int(bin(62)[2:])))
        elif char == '/':
            bitNum += ('%06d' % (int(bin(63)[2:])))
    for bitStart in range(0, len(bitNum), 8):
        decodingString += chr(int(bitNum[bitStart:bitStart+8], 2))
    print(f'#{tc} {decodingString}')


# 1979. 어디에 단어가 들어갈 수 있을까
def count_slots(line, K):
    count = 0
    result = 0
    for c in line+[0]:
        if c == 1:
            count += 1
        else:
            if count == K:
                result += 1
            count = 0
    return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nList = [list(map(int, input().split())) for _ in range(N)]
    rotatedNList = [list(row) for row in zip(*nList[::-1])]
    result = 0
    for i in range(N):
        result += count_slots(nList[i], K)
        result += count_slots(rotatedNList[i], K)
    print(f'#{tc} {result}')


# 1961. 숫자 배열 회전
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nList = [list(input().split()) for _ in range(n)]
    rotatedNList90 = [list(row) for row in zip(*nList[::-1])]
    rotatedNList180 = [list(row) for row in zip(*rotatedNList90[::-1])]
    rotatedNList270 = [list(row) for row in zip(*rotatedNList180[::-1])]
    print(f'#{tc}')
    for i in range(n):
        print(''.join(rotatedNList90[i]) + ' ' + ''.join(rotatedNList180[i]) + ' ' + ''.join(rotatedNList270[i]))


# 1974. 스도쿠 검증
def checkLine(line):
    return sorted(line) == ['1','2','3','4','5','6','7','8','9']

T = int(input())
for tc in range(1, T+1):
    board = [input().split() for _ in range(9)]
    ok = True

    for row in board:
        if not checkLine(row):
            ok = False
            break
    if ok:
        for col in zip(*board):
            if not checkLine(list(col)):
                ok = False
                break
    if ok:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = []
                for r in range(i, i+3):
                    block.extend(board[r][j:j+3])
                if not checkLine(block):
                    ok = False
                    break
            if not ok:
                break

    print(f'#{tc} {1 if ok else 0}')


# 2007. 패턴 마디의 길이
def isMadi(string, madi):
    if string[0:len(string)-(len(string) % len(madi))] == (madi) * (len(string)//len(madi)):
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    string = input().strip()
    for i in range(1, 11):
        madi = string[0:i]
        if isMadi(string, madi):
            print(f'#{tc} {i}')
            break


# 2005. 파스칼의 삼각형
def makeLine(pascal, lineNum):
    line = list()
    for num in range(lineNum):
        if num == 0 or num == (lineNum - 1):
            line.append(1)
        else:
            line.append(pascal[lineNum - 2][num-1] + pascal[lineNum - 2][num])
    return line



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascalTriangle = []
    print(f'#{tc}')
    for i in range(1, N+1):
        line = makeLine(pascalTriangle, i)
        print(*line)
        pascalTriangle.append(line)


# 1284. 수도 요금 경쟁
def chkAFee(p, w):
    return p * w

def chkBBFee(q, r, s, w):
    if r >= w:
        return q
    else:
        return q + s * (w-r)

T = int(input())
for tc in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    aFee = chkAFee(p, w)
    bFee = chkBBFee(q, r, s, w)
    print(f'#{tc} {aFee if aFee <= bFee else bFee}')


# 1989. 초심자의 회문 검사
def chkPalindrome(string):
    backString = string[::-1]
    if string == backString:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {1 if chkPalindrome(string) else 0}')


# 1959. 두 개의 숫자열
def chkMultiple(aList, bList):
    result = 0
    for i in range(len(aList)):
        result += (aList[i] * bList[i])
    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))
    if len(aList) > len(bList):
        cList = aList
        aList = bList
        bList = cList
    maxResult = 0
    for i in range(max(N, M) - min(N, M)+1):
        result = chkMultiple(aList, bList[i:i+len(aList)])
        maxResult = max(maxResult, result)
    print(f'#{tc} {maxResult}')


# 1288. 새로운 불면증 치료법
def chkNum(num):
    numStr = str(num)
    numSet = set(numStr)
    return numSet

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numSet = set()
    count = 1
    while True:
        try:
            numSet.update(chkNum(N*count))
            if numSet == {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                print(f'#{tc} {N*count}')
                break
            count += 1
        except Exception as e:
            print(e)
            break


# 1986. 지그재그 숫자
import math

def findResult(num):
    return math.ceil(num / 2) * (-1 if num % 2 == 0 else 1)

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    print(f'#{tc} {findResult(num)}')


# 1984. 중간 평균값 구하기
T = int(input())
for tc in range(1, T+1):
    nList = list(map(int, input().split()))
    nList.sort()
    average = round(sum(nList[1:len(nList)-1]) / (len(nList) - 2))
    print(f'#{tc} {average}')


# 1983. 조교의 성적 매기기
def calculTotalScore(score):
    return score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2

def chkGrade(N, rank):
    if N*0.1 >= rank:
        return 'A+'
    elif N*0.2 >= rank:
        return 'A0'
    elif N*0.3 >= rank:
        return 'A-'
    elif N*0.4 >= rank:
        return 'B+'
    elif N*0.5 >= rank:
        return 'B0'
    elif N*0.6 >= rank:
        return 'B-'
    elif N*0.7 >= rank:
        return 'C+'
    elif N*0.8 >= rank:
        return 'C0'
    elif N*0.9 >= rank:
        return 'C-'
    else:
        return 'D0'

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scoreList = list()
    resultScore = 0
    for i in range(N):
        score = list(map(int, input().split()))
        totalScore = calculTotalScore(score)
        scoreList.append(totalScore)
        if i == (K-1):
            resultScore = totalScore
    scoreList.sort(reverse=True)
    rank = scoreList.index(resultScore)+1
    print(f'#{tc} {chkGrade(N, rank)}')


# 1945. 간단한 소인수분해
def chkSquare(num, top):
    count = 0
    while True:
        try:
            if num % top == 0:
                count += 1
                num //= top
            else:
                break
        except Exception as e:
            print(e)
            break

    return num, count

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N, twoSquare = chkSquare(N, 2)
    N, threeSquare = chkSquare(N, 3)
    N, fiveSquare = chkSquare(N, 5)
    N, sevenSquare = chkSquare(N, 7)
    N, elevenSquare = chkSquare(N, 11)
    print(f'#{tc} {twoSquare} {threeSquare} {fiveSquare} {sevenSquare} {elevenSquare}')


# 1970. 쉬운 거스름돈
T = int(input())
for tc in range(1, T+1):
    money = int(input())
    print(f'#{tc}')
    change_50000 = money // 50000
    money %= 50000
    change_10000 = money // 10000
    money %= 10000
    change_5000 = money // 5000
    money %= 5000
    change_1000 = money // 1000
    money %= 1000
    change_500 = money // 500
    money %= 500
    change_100 = money // 100
    money %= 100
    change_50 = money // 50
    money %= 50
    change_10 = money // 10

    print(f'{change_50000} {change_10000} {change_5000} {change_1000} {change_500} {change_100} {change_50} {change_10}')

def calChange(money, unit):
    change = money // unit
    money %= unit
    return money, change

T = int(input())
for tc in range(1, T+1):
    money = int(input())
    print(f'#{tc}')
    money, change_50000 = calChange(money, 50000)
    money, change_10000 = calChange(money, 10000)
    money, change_5000 = calChange(money, 5000)
    money, change_1000 = calChange(money, 1000)
    money, change_500 = calChange(money, 500)
    money, change_100 = calChange(money, 100)
    money, change_50 = calChange(money, 50)
    change_10 = money // 10

    print(f'{change_50000} {change_10000} {change_5000} {change_1000} {change_500} {change_100} {change_50} {change_10}')

T = int(input())
for tc in range(1, T+1):
    money = int(input())
    units = (50000, 10000, 5000, 1000, 500, 100, 50, 10)
    changeList = list()
    for unit in units:
        change, money = divmod(money, unit)
        changeList.append(str(change))
    print(f"#{tc}")
    print(' '.join(changeList))


# 1966. 숫자를 정렬하자
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nList = list(map(int, input().split()))
    nList.sort()
    print(f'#{tc} '+' '.join(map(str, nList)))


# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    aList = list(map(int, input().split()))
    print(f'#{tc} {max(aList) - min(aList)}')


# 1940. 가랏! RC카!
def chkCmd(cmd, speed):
    if cmd[0] == 0:
        return speed
    elif cmd[0] == 1:
        return speed + cmd[1]
    elif cmd[0] == 2:
        return speed-cmd[1] if (speed-cmd[1] >= 0) else 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    distance = 0
    speed = 0
    for _ in range(N):
        cmd = list(map(int, input().split()))
        speed = chkCmd(cmd, speed)
        distance += speed
    print(f"#{tc} {distance}")


# 1946. 간단한 압축 풀기
import math

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    string = ''
    for _ in range(N):
        C, K = input().split()
        string += (C * int(K))
    print(f'#{tc}')
    for i in range(math.floor(len(string)/10)):
        print(string[i*10:(i+1)*10])
    if len(string) % 10 != 0:
        print(string[-1*(len(string) % 10):])


# 1948. 날짜 계산기
T = int(input())
lastDate = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    firMonth, firDate, secMonth, secDate = map(int, input().split())
    result = 0
    if firMonth == secMonth:
        result = secDate - firDate + 1
    else:
        result += (lastDate[firMonth-1] - firDate + 1)
        result += secDate
        for num in range(firMonth, secMonth-1):
            result += lastDate[num]
    print(f'#{tc} {result}')


# 1976. 시각 덧셈
T = int(input())
for tc in range(1, T+1):
    firHour, firMin, secHour, secMin = map(int, input().split())
    resultHour = firHour + secHour
    resultMin = firMin + secMin
    if resultMin >= 60:
        resultHour += 1
        resultMin -= 60
    if resultHour > 12:
        resultHour = (resultHour%12) if resultHour%12 != 0 else 12
    print(f'#{tc} {resultHour} {resultMin}')


# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    aList = list(map(int, input().split()))
    aSumList = [sum(aList[i:i+M]) for i in range(N-M+1)]
    result = max(aSumList) - min(aSumList)
    print(f'#{tc} {result}')


# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    aList = list(map(int, list(input())))
    resultNum = 0
    resultCount = 0
    for i in range(10):
        count = aList.count(i)
        if resultCount <= count:
            resultNum = i
            resultCount = count
    print(f'#{tc} {resultNum} {resultCount}')


# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
def calculSameArea(redArea, blueArea):
    resultArea = 0
    for row in range(10):
        for col in range(10):
            if redArea[row][col] == 1 and blueArea[row][col] == 2:
                resultArea += 1
    return resultArea

def fillArea(board, area, color):
    for row in range(area[1], area[3]+1):
        for col in range(area[0], area[2]+1):
            board[row][col] = color
    return board

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]
    redArea = [[0]*10 for _ in range(10)]
    blueArea = [[0]*10 for _ in range(10)]
    for i in range(N):
        area = list(map(int, input().split()))
        if area[4] == 1:
            redArea = fillArea(redArea, area, 1)
        else:
            blueArea = fillArea(blueArea, area, 2)
    resultArea = calculSameArea(redArea, blueArea)
    print(f'#{tc} {resultArea}')

#   두번째 방식
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]
    purple = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if board[row][col] != 3:
                    board[row][col] |= color
                    if board[row][col] == 3:
                        purple += 1
    print(f'#{tc} {purple}')


# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색
def binarySearch(l, r, key, count):
    c = int((l+r)/2)
    if c == key:
        return count
    elif c > key:
        return binarySearch(l, c, key, count+1)
    else:
        return binarySearch(c, r, key, count+1)

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    aCount = binarySearch(1, P, A, 1)
    bCount = binarySearch(1, P, B, 1)
    result = ''
    if aCount == bCount:
        result = '0'
    elif aCount > bCount:
        result = 'B'
    else:
        result = 'A'
    print(f"#{tc} {result}")


# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기
# 10 - 1
# 20 - 3
# 30 - 5
# 40 - 11
# 50 - 21
def calCount(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return calCount(N-10) + 2*calCount(N-20)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = calCount(N)
    print(f"#{tc} {result}")


# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
T = int(input())
for tc in range(1, T+1):
    n, string = input().split()
    resultString = ''
    for c in string:
        intC = int(c, 16)
        resultString += '%04d' % int(bin(intC)[2:])
    print(f'#{tc} {resultString}')


# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    print(f'#{tc} {1 if str1 in str2 else 0}')


# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
def chkPalindrome(arr, N):
    for i in range(len(arr)-N+1):
        if arr[i:i+N] == arr[i:i+N][::-1]:
            return arr[i:i+N]
    return ''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stringList = [list(input()) for i in range(N)]
    colrowStringList = list(zip(*stringList))
    for row in range(N):
        isStringListPal = chkPalindrome(stringList[row], M)
        iscolrowStringListPal = chkPalindrome(colrowStringList[row], M)
        if isStringListPal != '':
            print(f"#{tc} {''.join(isStringListPal)}")
            break
        elif iscolrowStringListPal != '':
            print(f"#{tc} {''.join(iscolrowStringListPal)}")
            break
    else:
        print('Palindrome이 존재하지 않습니다.')