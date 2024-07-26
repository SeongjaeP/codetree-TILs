# 좌표 정하기
# 겹치는지 체크



# 최대값 갱신


n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def clear_board():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0

def draw(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            visited[i][j] += 1

def check_board():
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                return True
    return False

def overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return check_board()

def rect_sum(x1, y1, x2, y2):
    return sum([board[i][j] for i in range(x1, x2 + 1) for j in range(y1, y2 + 1)])

def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = -float('INF')

    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum , rect_sum(x1, y1, x2, y2)+
                                                rect_sum(i, j, k, l))

    return max_sum

def find_max_sum():
    max_sum = -float('INF')
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_sum = max(max_sum, find_max_sum_with_rect(i, j, k, l))
    return max_sum

ans = find_max_sum()
print(ans)