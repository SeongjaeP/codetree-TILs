n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def spread_dust():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    temp_board = [[0] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if board[x][y] > 0:
                messy_diff = board[x][y] // 5
                count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != -1:
                        temp_board[nx][ny] += messy_diff
                        count += 1
                board[x][y] -= messy_diff * count

    for x in range(n):
        for y in range(m):
            board[x][y] += temp_board[x][y]


wind = []
for i in range(n):
    if board[i][0] == -1:
        wind.append((i, 0))


def wind_move():
    u_x, u_y = wind[0]
    d_x, d_y = wind[1]

    # 위쪽 공기 청정기 (반시계 방향)
    # 아래로 이동
    for i in range(u_x - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    # 왼쪽에서 오른쪽으로 이동
    for i in range(m - 1):
        board[0][i] = board[0][i + 1]
    # 아래에서 위로 이동
    for i in range(u_x):
        board[i][m - 1] = board[i + 1][m - 1]
    # 오른쪽에서 왼쪽으로 이동
    for i in range(m - 1, 1, -1):
        board[u_x][i] = board[u_x][i - 1]
    board[u_x][1] = 0

    # 아래쪽 공기 청정기 (시계 방향)
    # 위로 이동
    for i in range(d_x + 1, n - 1):
        board[i][0] = board[i + 1][0]
    # 왼쪽에서 오른쪽으로 이동
    for i in range(m - 1):
        board[n - 1][i] = board[n - 1][i + 1]
    # 위에서 아래로 이동
    for i in range(n - 1, d_x, -1):
        board[i][m - 1] = board[i - 1][m - 1]
    # 오른쪽에서 왼쪽으로 이동
    for i in range(m - 1, 1, -1):
        board[d_x][i] = board[d_x][i - 1]
    board[d_x][1] = 0


for _ in range(k):
    spread_dust()
    wind_move()


result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] > 0:
            result += board[i][j]

print(result)