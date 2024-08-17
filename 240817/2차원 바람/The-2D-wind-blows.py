# N * M에 Q번 바람이 붐

# 경계에 있는 숫자들을 시계 방향으로 한 칸씩 shift
from collections import deque

def in_range(r, c):
    return 0 <= r< n and 0 <=c < m

def get_grids(r1,c1,r2,c2):
    queue = deque([])
    for col in range(c1, c2+ 1):
        queue.append((r1, col))
    for row in range(r1+1, r2+1):
        queue.append((row, c2))
    for col in range(c2 - 1, c1 - 1, -1):
        queue.append((r2, col))
    for row in range(r2 - 1, r1, -1):
        queue.append((row, c1))
    return queue


def simulate(r1, c1, r2, c2):
    temps = deque([])
    for r, c in get_grids(r1, c1, r2, c2):
        temps.append(board[r][c])
    temps.rotate(1)
    for idx, (r, c) in enumerate(get_grids(r1, c1, r2, c2)):
        board[r][c] = temps[idx]
    diffusion_board = [[0 for _ in range(m)] for _ in range(n)]

    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            sum_val = board[r][c]
            cnt = 1
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr,nc):
                    cnt += 1
                    sum_val += board[nr][nc]
            sum_val = sum_val // cnt
            diffusion_board[r][c] = sum_val
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            board[r][c] = diffusion_board[r][c]

n, m, q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
for _ in range(q):
    r1, c1, r2, c2 = map(int,input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    simulate(r1, c1, r2, c2)

for row in board:
    print(*row)