# T = int(input().strip())
# for tc in range(1, T + 1):
#     N = int(input().strip())
#     prices = list(map(int, input().split()))
#
#     max_future = 0
#     profit = 0
#
#     for p in reversed(prices):
#         if p >= max_future:
#             max_future = p
#         else:
#             profit += (max_future - p)
#
#     print(f"#{tc} {profit}")
#
#
# T = int(input().strip())
# for tc in range(1, T + 1):
#     N = int(input().strip())
#     board = [[0] * N for _ in range(N)]
#     dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     d = 0
#     r, c = 0, 0
#
#     for num in range(1, N * N + 1):
#         board[r][c] = num
#         nr, nc = r + dirs[d][0], c + dirs[d][1]
#
#         if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] != 0:
#             d = (d + 1) % 4
#             nr, nc = r + dirs[d][0], c + dirs[d][1]
#
#         r, c = nr, nc
#
#     print(f"#{tc}")
#     for row in board:
#         print(' '.join(map(str, row)))
#
#
# # 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
# from collections import defaultdict
# T = int(input())
# for tc in range(1, T + 1):
#     tcNum = input()
#     scoreList = list(map(int, input().split()))
#     scoreDict = defaultdict(int)
#     for score in scoreList:
#         scoreDict[score] += 1
#     manyScore = sorted(scoreDict.items(), key=(lambda x:(x[1], x[0])), reverse=True)
#     print(f'#{tcNum} '+ str(manyScore[0][0]))
#
#
# # 2001. 파리 퇴치
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().strip().split())
#     maxPari = 0
#     nList = list()
#     for n in range(1, N + 1):
#         num = list(map(int, input().split()))
#         nList.append(num)
#     for xStart in range((N-M+1)):
#         for yStart in range((N-M+1)):
#             pari = 0
#             for x in range(M):
#                 for y in range(M):
#                     pari += nList[xStart + x][yStart + y]
#             if pari > maxPari:
#                 maxPari = pari
#     print(f'#{tc} '+ str(maxPari))
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_sum = 0
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             s = 0
#             for x in range(M):
#                 s += sum(arr[i + x][j:j + M])
#             max_sum = max(max_sum, s)
#
#     print(f"#{tc} {max_sum}")
#
#
# # 1926. 간단한 369게임
# def trannum(n):
#     nStr = str(n)
#     if '3' in nStr or '6' in nStr or '9' in nStr:
#         nStr = '-' * (nStr.count('3') + nStr.count('6') + nStr.count('9'))
#     return nStr
#
# N = int(input())
# for num in range(1, N+1):
#     print(trannum(num), end = ' ')
#
#
# # 1928. Base64 Decoder
# T = int(input())
# for tc in range(1, T+1):
#     string = input()
#     bitNum = ''
#     decodingString = ''
#     for char in string:
#         if char.isupper():
#             bitNum += ('%06d' % (int(bin(ord(char) - 65)[2:])))
#         elif char.islower():
#             bitNum += ('%06d' % (int(bin(ord(char) - 71)[2:])))
#         elif char.isdigit():
#             bitNum += ('%06d' % (int(bin(ord(char) +4)[2:])))
#         elif char == '+':
#             bitNum += ('%06d' % (int(bin(62)[2:])))
#         elif char == '/':
#             bitNum += ('%06d' % (int(bin(63)[2:])))
#     for bitStart in range(0, len(bitNum), 8):
#         decodingString += chr(int(bitNum[bitStart:bitStart+8], 2))
#     print(f'#{tc} {decodingString}')
#
#