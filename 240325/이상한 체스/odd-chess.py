from itertools import product

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]

cctvs = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))

def watch(x, y, direction, temp):
    dx, dy = directions[direction]
    while True:
        x, y = x + dx, y + dy
        if x < 0 or x >= n or y < 0 or y >= m or office[x][y] == 6:
            break
        if temp[x][y] == 0:
            temp[x][y] = -1

def dfs(depth, office):
    if depth == len(cctvs):
        return sum(row.count(0) for row in office)

    x, y, type = cctvs[depth]
    result = float('inf')
    
    for direction in product(range(4), repeat=(4 if type == 5 else type)):
        temp = [row[:] for row in office]
        if type == 1:
            for d in direction:
                watch(x, y, d, temp)
        elif type == 2:
            for d in [direction[0], (direction[0] + 2) % 4]:
                watch(x, y, d, temp)
        elif type == 3:
            for d in direction[:2]:
                watch(x, y, d, temp)
        elif type == 4:
            for d in direction[:3]:
                watch(x, y, d, temp)
        elif type == 5:
            for d in direction:
                watch(x, y, d, temp)
        
        result = min(result, dfs(depth + 1, temp))
    return result

print(dfs(0, office))