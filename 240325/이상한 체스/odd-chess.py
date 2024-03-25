import copy

n, m = map(int, input().split())
map_matrix = [list(map(int, input().split())) for _ in range(n)]
chess = [(i, j, map_matrix[i][j]) for i in range(n) for j in range(m) if map_matrix[i][j] in [1, 2, 3, 4, 5]]

directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def fill(map_matrix, x, y, directions):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < n and 0 <= ny < m) or map_matrix[nx][ny] == 6:
                break
            elif map_matrix[nx][ny] == 0:
                map_matrix[nx][ny] = -1

def dfs(depth, map_matrix):
    if depth == len(chess):
        return sum(row.count(0) for row in map_matrix)

    x, y, type = chess[depth]
    result = float('inf')
    for direction in directions[type]:
        tmp = copy.deepcopy(map_matrix)
        fill(tmp, x, y, direction)
        result = min(result, dfs(depth + 1, tmp))
    return result

print(dfs(0, map_matrix))