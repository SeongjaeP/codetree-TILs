n, m, k = map(int, input().split())
nul_map = [list(map(int, input().split())) for _ in range(n)]
virus = [[[] for _ in range(n)] for _ in range(n)]
init_nul = [[5] * n for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    virus[x-1][y-1].append(age)

# 왼쪽 대각선부터 반시계 방향으로
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if virus[i][j]:
                virus[i][j].sort()
                survived = []
                dead_nut = 0
                for age in virus[i][j]:
                    if init_nul[i][j] >= age:
                        init_nul[i][j] -= age
                        survived.append(age + 1)

                    else:
                        dead_nut += age // 2
                virus[i][j] = survived
                init_nul[i][j] += dead_nut

    
    for i in range(n):
        for j in range(n):
            for age in virus[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            virus[nx][ny].append(1)

    
    for i in range(n):
        for j in range(n):
            init_nul[i][j] += nul_map[i][j]




count = sum(len(cell) for row in virus for cell in row)
print(count)