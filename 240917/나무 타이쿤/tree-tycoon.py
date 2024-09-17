# n, m = map(int,input().split())
# matrix_map = [list(map(int,input().split())) for _ in range(n)]
# move_map = [tuple(map(int,input().split())) for _ in range(m)]
# init_tree = [(n-2,0), (n-2,1), (n-1,0), (n-1,1)]

# #  1부터 고려해야하니 0을 채워줌
# # dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# # dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]
# # direction = [(0,0), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)]
# # diag = [(-1,-1), (1,-1), (1,1), (-1,1)] 

# dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]
# diag = [(-1,-1), (1,-1), (1,1), (-1,1)] 

# def move(init_tree):
#     for i in range(4):
#         bx, by = init_tree[i]
#         nbx, nby = (bx + dx[move_map[0]] * move_map[1]) % n, (by + dy[move_map[0]] * move_map[1]) % n
#         init_tree[i] = nbx, nby
#         matrix_map[nbx][nby] += 1

#     for (nx, ny) in init_tree:
#         for diag in diag:
#             gx, gy = nx + diag[0], ny + diag[1]
#             if 0 <= gx < n and 0 <= gy < n and matrix_map[gx][gy] > 0:
#                 matrix_map[gx][gy] += 1
#     return init_tree

# def cut(matrix_map):
#     for i in range(n):
#         for j in range(n):
#             if matrix_map[i][j] >= 2:
#                 matrix_map[i][j] -= 2

#     return matrix_map
    

# for _ in range(m):
#     init_tree = move(init_tree)
#     matrix_map = cut(matrix_map)
    
# # 점수 췤

# def upscore():
#     summ = 0
#     for i in range(n):
#         for j in range(n):
#             summ += matrix_map[i][j]
#     print(summ)
    
# upscore()


def getInput():
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    movelist = [tuple(map(int,input().split())) for _ in range(m)]

    return n, m, graph, movelist

def moveandgrow(nutrients, move):
    # 움직이고 키우는 함수
    direction = [(0,0),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
    # 1부터 시작이니 앞에 의미없는 요소 한개 추가
    growlist = [(-1,-1),(-1,1),(1,1),(1,-1)]  # 대각선

    for i in range(len(nutrients)):
        x, y = nutrients[i]
        nx, ny = (x+direction[move[0]][0]*move[1])%n, (y+direction[move[0]][1]*move[1])%n
        nutrients[i] = (nx, ny)
        
        # 자라는 파트
        graph[nx][ny] += 1

    for (nx, ny) in nutrients:
        for grow in growlist:
            gx, gy = nx+grow[0], ny+grow[1]
            if 0<=gx<n and 0<=gy<n and graph[gx][gy]>0:
                graph[nx][ny] += 1

    return nutrients

def cut():
    newnutrients = []
    for x in range(n):
        for y in range(n):
            if (x,y) not in nutrients and graph[x][y] > 1:
                graph[x][y] -= 2
                newnutrients.append((x, y))
    return newnutrients

def answer():
    summ = 0
    for x in range(n):
        for y in range(n):
            summ += graph[x][y]
    print(summ)


n, m, graph, movelist = getInput()
nutrients = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]

for time in range(m):
    # m년 동안 moveandgrow와 cut에 따라 바뀌는 영양제 좌표를 업데이트.

    nutrients = moveandgrow(nutrients, movelist[time])
    nutrients = cut()

answer()