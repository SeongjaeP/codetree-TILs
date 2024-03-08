# 중간에 못 풀어서 아래 링크 클론코딩했습니다..
# https://wikidocs.net/216602

from collections import deque

def getInput():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return n, m, matrix

def move (n, matrix, dir, x, y, row, column):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    nx, ny = x + direction[dir][0], y + direction[dir][1]
    if nx < 0 or nx == n or ny < 0 or ny == n:
        dir = (dir + 2) % 4
        nx, ny = x + direction[dir][0], y + direction[dir][1]

    if dir == 0:
        row.rotate(1)
        column[0] = column[0]
        column[2] = row[2]
    elif dir == 1:
        column.rotate(-1)
        row[0] = column[0]
        row[2] = column[2]
    elif dir == 2:
        row.rotate(1)
        column[0] = row[0]
        column[2] = row[2]
    elif dir == 3:
        column.rotate(1)
        row[0] = column[0]
        row[2] = column[2]

    if row[2] > matrix[nx][ny]:
        dir = (dir + 1) % 4
    elif row[2] < matrix[nx][ny]:
        dir = (dir + 3) % 4

    return dir, nx, ny, row, column


def score(n, matrix, dir, x, y):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = matrix[x][y]
    q = deque([(x,y)])
    llist = {(x,y)}
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == start and (nx, ny) not in llist:
                cnt += 1
                q.append((nx, ny))
                llist.add((nx, ny))

    return start * cnt


def main():
    n, m, matrix = getInput()
    x, y = 0, 0
    dir = 0
    row = deque([1, 3, 6, 4])
    column = deque([1, 5, 6, 2])
    answer = 0

    for _ in range(m):
        dir, x, y, row, column = move(n, matrix, dir, x, y, row, column)
        answer += score(n, matrix, dir, x, y)

    print(answer)

main()