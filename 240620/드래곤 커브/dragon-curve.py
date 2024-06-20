# 못 풀어서 아래 링크 참고했습니다
# https://tmdrl5779.tistory.com/146

n = int(input())
graph = [[0] * 101 for _ in range(101)]


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1

    curve = [d]
    for _ in range(g):
        for i in range(len(curve) -1, -1, -1):
            curve.append((curve[i] + 1) % 4)

    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        
        graph[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            answer += 1

print(answer)