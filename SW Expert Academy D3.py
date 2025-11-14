# 1206. [S/W 문제해결 기본] 1일차 - View
for tc in range(1, 11):
    N = int(input())
    buildingList = list(map(int, input().split()))
    result = 0
    for idx in range(2, len(buildingList)-1):
        building = buildingList[idx]
        buildings = buildingList[idx-2:idx] + buildingList[idx+1:idx+3]
        maxSurroundHeight = max(buildings)
        result += max(building - maxSurroundHeight, 0)
    print(f'#{tc} {result}')


# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
def solve_case(num_str, K):
    n = len(num_str)
    visited = [set() for _ in range(K+1)]
    best = ['0']

    def dfs(s, d):
        if d == K:
            if s > best[0]:
                best[0] = s
            return
        if s in visited[d]:
            return
        visited[d].add(s)

        s_list = list(s)
        for i in range(n-1):
            for j in range(i+1, n):
                s_list[i], s_list[j] = s_list[j], s_list[i]
                dfs(''.join(s_list), d+1)
                s_list[i], s_list[j] = s_list[j], s_list[i]

    dfs(num_str, 0)
    return best[0]

T = int(input())
for tc in range(1, T+1):
    num_str, K = input().split()
    K = int(K)
    ans = solve_case(num_str, K)
    print(f'#{tc} {ans}')


# 1208. [S/W 문제해결 기본] 1일차 - Flatten
def dump():
    maxHhtIdx = heightList.index(max(heightList))
    minHhtIdx = heightList.index(min(heightList))
    heightList[maxHhtIdx] -= 1
    heightList[minHhtIdx] += 1
    return

for tc in range(1, 11):
    dumpCount = int(input())
    heightList = list(map(int, input().split()))
    for _ in range(dumpCount):
        dump()
    print(f'#{tc} {max(heightList)-min(heightList)}')


# 1209. [S/W 문제해결 기본] 2일차 - Sum
for tc in range(1, 11):
    number = int(input())
    board = []
    maxSum = 0
    for row in range(100):
        numList = list(map(int, input().split()))
        maxSum = max(maxSum, sum(numList))
        board.append(numList)
    transitionBoard = list(zip(*board))
    sumLeftToRightDiagonal = 0
    sumRightToLeftDiagonal = 0
    for row in range(100):
        maxSum = max(maxSum, sum(transitionBoard[row]))
        sumLeftToRightDiagonal += board[row][row]
        sumRightToLeftDiagonal += board[row][99-row]
    maxSum = max(maxSum, sumLeftToRightDiagonal, sumRightToLeftDiagonal)
    print(f'#{tc} {maxSum}')


# 2805. 농작물 수확하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    for idx in range(N//2):
        result += sum(board[idx][(N//2)-idx:-1*(N//2-idx)])
    result += sum(board[N//2])
    for idx in range(N//2):
        result += sum(board[N//2+1+idx][idx+1:N-idx-1])
    print(f'#{tc} {result}')


# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
def chkCode(keyCode):
    keyCodeString = ''.join(keyCode)
    if keyCodeString == '0001101':
        return 0
    elif keyCodeString == '0011001':
        return 1
    elif keyCodeString == '0010011':
        return 2
    elif keyCodeString == '0111101':
        return 3
    elif keyCodeString == '0100011':
        return 4
    elif keyCodeString == '0110001':
        return 5
    elif keyCodeString == '0101111':
        return 6
    elif keyCodeString == '0111011':
        return 7
    elif keyCodeString == '0110111':
        return 8
    else:
        return 9

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    keyCode = []
    decodeCode = []
    findKeyCode = False
    for i in range(N):
        code = list(input())
        if '1' in code and not findKeyCode:
            keyCode = code[::-1]
            keyCode = keyCode[keyCode.index('1'):keyCode.index('1')+56]
            keyCode = keyCode[::-1]
            findKeyCode = True
    for idx in range(0, 56, 7):
        num = chkCode(keyCode[idx:idx+7])
        decodeCode.append(num)
    if (sum(decodeCode[::2])*3 + sum(decodeCode[1::2])) % 10 == 0:
        print(f'#{tc} {sum(decodeCode)}')
    else:
        print(f'#{tc} 0')


# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
from collections import deque

for i in range(1, 11):
    tc = int(input())
    numList = deque(map(int,input().split()))
    count = 1

    while True:
        if 0 in numList:
            break
        firNum = numList.popleft()
        numList.append((firNum-count) if firNum-count >= 0 else 0)
        count = (count % 5) + 1
    print(f'#{tc} ', end='')
    print(*numList)


# 1215. [S/W 문제해결 기본] 3일차 - 회문1
def countPalindromeInBoard(board, length):
    count = 0
    for row in range(8):
        for col in range(8-length+1):
            string = ''.join(board[row][col:col+length])
            backString = string[::-1]
            if string == backString:
                count += 1
    return count


for tc in range(1, 11):
    length = int(input())
    board = [list(input()) for _ in range(8)]
    countWeight = countPalindromeInBoard(board, length)
    transitionBoard = list(zip(*board))
    countHeight = countPalindromeInBoard(transitionBoard, length)
    print(f'#{tc} {countWeight+countHeight}')