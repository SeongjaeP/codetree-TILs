from collections import deque

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

w = deque([1,3,6,4])
h = deque([1,2,6,5])

def move_dice(x,y,dir,w,h,n):

    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    nx, ny = x + direction[dir][0], y + direction[dir][1]
    # 부딪힐 경우
    if nx == n or ny == n or nx < 0 or ny < 0:
        # 방향전환 필요 dir 
        dir = (dir+2) % 4
        nx, ny = x + direction[dir][0], y + direction[dir][1]

    if dir == 0:
        w.rotate(1)
        # w = 4 1 3 6
        1,2,6,5

        # h = 4 2 3 5
        h[0] = w[0]
        h[2] = w[2]

    elif dir == 1:
        h.rotate(1)
        #w = deque([1,3,6,4])
        # w = 5 3 2 4
        # h = 5 1 2 6
        w[0] = h[0]
        w[2] = h[2]
    
    elif dir == 2:
        w.rotate(-1)
        # w = 3 6 4 1
        #h = deque([1,2,6,5])
        # h = 3 2 4 5
        h[0] = w[0]
        h[2] = w[2]

    elif dir == 3:
        h.rotate(-1)
        #w = deque([1,3,6,4])
        # h = 2 6 5 1
        # w = 2 3 5 4
        w[0] = h[0]
        w[2] = h[2]

    # 방향전환 시계방향, 반시계방향 정하기
    if w[2] > board[nx][ny]:
        dir = (dir+1) % 4 # 시계방향 회전
    
    elif w[2] < board[nx][ny]:
        dir = (dir+3) % 4 # 반시계방향 회전

    return nx, ny, dir, w, h
    


# 점수계산
def bfs(x,y,board,dir,n):

    visited = [[False] * n for _ in range(n)]
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    start_val = board[x][y]
    visited[x][y] = True
    queue = deque([(x,y)])
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == start_val and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return start_val * cnt


ans = 0
x, y, dir = 0, 0, 0
for _ in range(m):
    x, y, dir, w, h = move_dice(x,y,dir,w,h,n)
    ans += bfs(x,y,board,dir,n)
print(ans)