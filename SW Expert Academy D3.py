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


# 5215. 햄버거 다이어트
def dfs(ingrediIdx, totalScore, totalCal):
    global maxScore

    if totalCal > limitCal:
        return

    if ingrediIdx == ingrediCount:
        if maxScore < totalScore:
            maxScore = totalScore
        return

    dfs(ingrediIdx+1, totalScore, totalCal)
    dfs(ingrediIdx+1, totalScore+ingrediList[ingrediIdx][0], totalCal+ingrediList[ingrediIdx][1])

T = int(input())
for tc in range(1, T+1):
    ingrediCount, limitCal = map(int, input().split())
    ingrediList = []
    for i in range(ingrediCount):
        score, cal = map(int, input().split())
        ingrediList.append((score, cal))
    maxScore = 0
    dfs(0, 0, 0)

    print(f'#{tc} {maxScore}')


# 2806. N-Queen
def solve_n_queen(N):
    col = [False] * N
    diag1 = [False] * (2*N)
    diag2 = [False] * (2*N)
    answer = 0

    def dfs(row):
        nonlocal answer
        if row == N:
            answer += 1
            return

        for c in range(N):
            if col[c]:
                continue
            if diag1[row + c]:
                continue
            if diag2[row - c + N - 1]:
                continue

            col[c] = True
            diag1[row + c] = True
            diag2[row - c + N - 1] = True

            dfs(row + 1)

            col[c] = False
            diag1[row + c] = False
            diag2[row - c + N - 1] = False

    dfs(0)
    return answer

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = solve_n_queen(N)
    print(f"#{tc} {result}")


# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
for tc in range(1, 11):
    length = int(input())
    board = [list(map(int, input().split())) for _ in range(length)]
    visited = [[False] * length for _ in range(length)]
    result = 0
    for row in range(length):
        for col in range(length):
            if board[row][col] == 0:
                continue
            elif board[row][col] == 1:
                # 아래로 이동해야 함.
                if row >= length-1:
                    board[row][col] = 0
                    continue
                if not visited[row][col] and board[row+1][col] == 0:
                    visited[row+1][col] = True
                    board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
            else:
                if row <= 0:
                    board[row][col] = 0
                    continue
                # 위로 이동해야 함.
                if board[row-1][col] == 0:
                    board[row][col], board[row-1][col] = board[row-1][col], board[row][col]
        visited = [[False] * length for _ in range(length)]
    board = list(zip(*board))
    for line in board:
        line = ''.join(map(str, line))
        result += line.count('12')
    print(f'#{tc} {result}')


# 1289. 원재의 메모리 복구하기
T = int(input())
for tc in range(1, T+1):
    string = input()
    result = 0
    for idx in range(len(string)):
        if string.count('1') == 0:
            break
        if string[idx] == '0':
            continue
        else:
            string = string[:idx] + string[idx:].replace('0', '3').replace('1', '0').replace('3', '1')
            result += 1
    print(f'#{tc} {result}')
# 다른 방식
T = int(input())
for tc in range(1, T+1):
    s = input().strip()
    now = '0'
    cnt = 0
    for ch in s:
        if ch != now:
            cnt += 1
            now = ch
    print(f'#{tc} {cnt}')


# 1213. [S/W 문제해결 기본] 3일차 - String
for t in range(10):
    tc = int(input())
    keyword = input()
    string = input()
    print(f'#{tc} {string.count(keyword)}')


# 1216. [S/W 문제해결 기본] 3일차 - 회문2
def chkPalindrome(board):
    global maxLength
    for row in range(100):
        for col in range(100):
            for length in range(2, 100):
                string = board[row][col:col+length]
                backString = string[::-1]
                if string == backString:
                    maxLength = max(maxLength, len(string))

for _ in range(10):
    tc = int(input())
    board = [input().strip() for _ in range(100)]
    maxLength = 1
    transitionBoard = list(zip(*board))
    chkPalindrome(board)
    chkPalindrome(transitionBoard)
    print(f'#{tc} {maxLength}')


# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
def multiple(n, m):
    if m == 1:
        return n
    return n * multiple(n, m-1)

for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    result = 1
    print(f'#{tc} {multiple(N, M)}')


# 1873. 상호의 배틀필드
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    mapList = []
    dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    carLoc = [0, 0]
    carDir = dirs[0]
    for i in range(H):
        line = list(input())
        mapList.append(line)
        if '^' in line:
            carLoc = [i, line.index('^')]
            carDir = dirs[3]
        elif 'v' in line:
            carLoc = [i, line.index('v')]
            carDir = dirs[1]
        elif '<' in line:
            carLoc = [i, line.index('<')]
            carDir = dirs[2]
        elif '>' in line:
            carLoc = [i, line.index('>')]
            carDir = dirs[0]
    N = int(input())
    cmdList = list(input())
    transitionMapList = list(zip(*mapList))
    for cmd in cmdList:
        if cmd == 'U':
            carDir = dirs[3]
            mapList[carLoc[0]][carLoc[1]] = '^'
            if carLoc[0]-1 >= 0 and mapList[carLoc[0]-1][carLoc[1]] == '.':
                mapList[carLoc[0]][carLoc[1]], mapList[carLoc[0]-1][carLoc[1]] = mapList[carLoc[0]-1][carLoc[1]], mapList[carLoc[0]][carLoc[1]]
                carLoc[0] -= 1
        elif cmd == 'D':
            carDir = dirs[1]
            mapList[carLoc[0]][carLoc[1]] = 'v'
            if carLoc[0]+1 <= (H-1) and mapList[carLoc[0]+1][carLoc[1]] == '.':
                mapList[carLoc[0]][carLoc[1]], mapList[carLoc[0]+1][carLoc[1]] = mapList[carLoc[0]+1][carLoc[1]], mapList[carLoc[0]][carLoc[1]]
                carLoc[0] += 1
        elif cmd == 'L':
            carDir = dirs[2]
            mapList[carLoc[0]][carLoc[1]] = '<'
            if carLoc[1]-1 >= 0 and mapList[carLoc[0]][carLoc[1]-1] == '.':
                mapList[carLoc[0]][carLoc[1]], mapList[carLoc[0]][carLoc[1]-1] = mapList[carLoc[0]][carLoc[1]-1], mapList[carLoc[0]][carLoc[1]]
                carLoc[1] -= 1
        elif cmd == 'R':
            carDir = dirs[0]
            mapList[carLoc[0]][carLoc[1]] = '>'
            if carLoc[1] + 1 <= (W-1) and mapList[carLoc[0]][carLoc[1] + 1] == '.':
                mapList[carLoc[0]][carLoc[1]], mapList[carLoc[0]][carLoc[1] + 1] = mapList[carLoc[0]][carLoc[1] + 1], mapList[carLoc[0]][carLoc[1]]
                carLoc[1] += 1
        elif cmd == 'S':
            if carDir == dirs[0]:
                line = mapList[carLoc[0]]
                for i in range(carLoc[1]+1, W):
                    if line[i] == '*':
                        mapList[carLoc[0]][i] = '.'
                        break
                    elif line[i] == '#':
                        break
            elif carDir == dirs[1]:
                line = transitionMapList[carLoc[1]]
                for i in range(carLoc[0]+1, H):
                    if line[i] == '*':
                        mapList[i][carLoc[1]] = '.'
                        transitionMapList = list(zip(*mapList))
                        break
                    elif line[i] == '#':
                        break
            elif carDir == dirs[2]:
                line = mapList[carLoc[0]]
                for i in range(carLoc[1]-1, -1, -1):
                    if line[i] == '*':
                        mapList[carLoc[0]][i] = '.'
                        break
                    elif line[i] == '#':
                        break
            elif carDir == dirs[3]:
                line = transitionMapList[carLoc[1]]
                for i in range(carLoc[0] - 1, -1, -1):
                    if line[i] == '*':
                        mapList[i][carLoc[1]] = '.'
                        transitionMapList = list(zip(*mapList))
                        break
                    elif line[i] == '#':
                        break
    print(f'#{tc}', end=' ')
    for idx in range(H):
        print(''.join(mapList[idx]))


# 1228. [S/W 문제해결 기본] 8일차 - 암호문1
for tc in range(1, 11):
    N = int(input())
    originalList = list(input().split())
    cmdCount = int(input())
    cmdList = list(input().split())
    for idx in range(len(cmdList)):
        count = 0
        if cmdList[idx] == 'I':
            loc = int(cmdList[idx+1])
            if loc >= 10:
                continue
            count = int(cmdList[idx+2])
            numList = cmdList[idx+3:idx+3+count]
            originalList = originalList[:loc] + numList + originalList[loc:]
        idx += 2+count
    print(f'#{tc} ' + ' '.join(originalList[:10]))


# 1230. [S/W 문제해결 기본] 8일차 - 암호문3
for tc in range(1, 11):
    N = int(input())
    originalList = list(input().split())
    cmdCount = int(input())
    cmdList = list(input().split())
    for idx in range(len(cmdList)):
        count = 0
        if cmdList[idx] == 'I':
            loc = int(cmdList[idx+1])
            count = int(cmdList[idx+2])
            numList = cmdList[idx+3:idx+3+count]
            originalList = originalList[:loc] + numList + originalList[loc:]
            idx += 2+count
        elif cmdList[idx] == 'D':
            loc = int(cmdList[idx+1])
            count = int(cmdList[idx+2])
            originalList = originalList[:loc] + originalList[loc+count:]
            idx += 2
        elif cmdList[idx] == 'A':
            count = int(cmdList[idx+1])
            numList = cmdList[idx+2:idx+2+count]
            originalList.extend(numList)
            idx += 1 + count
    print(f'#{tc} ' + ' '.join(originalList[:10]))


# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    chargers.sort()

    pos = 0
    count = 0

    while pos + K < N:
        next_pos = pos
        for c in chargers:
            if pos < c <= pos + K:
                next_pos = c
        if next_pos == pos:
            count = 0
            break
        pos = next_pos
        count += 1

    print(f"#{tc} {count}")


# 4615. 재미있는 오셀로 게임
def makeInitBoard(N):
    board = [[0]*N for _ in range(N)]
    mid = N // 2
    board[mid-1][mid-1] = 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1
    board[mid][mid] = 2
    return board

def placeStone(r, c, color):
    board[r][c] = color
    opp = 2 if color == 1 else 1

    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        to_flip = []

        while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == opp:
            to_flip.append((nr, nc))
            nr += dr
            nc += dc

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == color:
            for fr, fc in to_flip:
                board[fr][fc] = color

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = makeInitBoard(N)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]
    blackCount = 0
    whiteCount = 0
    for _ in range(M):
        locCol, locRow, color = map(int, input().split())
        placeStone(locRow-1, locCol-1, color)
    for i in range(N):
        blackCount += board[i].count(1)
        whiteCount += board[i].count(2)
    print(f'#{tc} {blackCount} {whiteCount}')