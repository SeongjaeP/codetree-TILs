n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def check_board(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] < 0:
                return -1
    return (x2 - x1 + 1) * (y2 - y1 + 1)

def find_max_rec():
    max_area = 0
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    area = check_board(x1, y1, x2, y2)
                    if area != -1:
                        max_area = max(max_area, area)
                        
    return max_area if max_area > 0 else -1

max_size = find_max_rec()
print(max_size)