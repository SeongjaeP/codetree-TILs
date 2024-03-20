# 왼쪽 방향으로 방문 안했으면 왼쪽으로 꺽고 1칸 전진
# 방문 처리 할 것
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**4)

n, m = map(int, input().split())
x, y, d = map(int, input().split())
car_matrix = [list(map(int, input().split())) for _ in range(n)]

#      0  1 2  3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
car_matrix[x][y] = 2
result = 1

def dfs(x, y, d, d_cnt=0):
    global result
    # d_cnt가 4이면 전진하지 못했으니까 d를 유지하면서 뒤로 한칸.
    if d_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < n and 0 <= ny < m and car_matrix[nx][ny] != 1: 
            dfs(nx, ny, d, 0)
        else: # 후진까지 했는데 갈 곳이 없으면 끝내
            return
    else:
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m and car_matrix[nx][ny] == 0:
            car_matrix[nx][ny] = 2
            result += 1
            dfs(nx, ny, nd, 0)
        else:
            dfs(x, y, nd, d_cnt + 1)
        
dfs(x, y, d, 0)
print(result)