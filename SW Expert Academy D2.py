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