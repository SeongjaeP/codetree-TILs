# '''
# 각 칸은 빈칸, 함정, 또는 벽으로 구성되어있음. 체스판 밖도 벽으로 간주

# 마력으로 상대방을 밀쳐낼 수 있다. 
# 각 기사는 초기위치가 (r,c)로 주어짐. 방패가 h x w 크기의 직사각형 형태. 체력은 k
# '''

# # 기사 이동
# '''
# 상하좌우로 이동가능
# 이동하려는 위치에 기사가 있으면 밀려남 -> while문
# 방향 끝에 벽이 있으면 모든 기사가 이동 불가능 
# 체스판에서 사라진다는게 뭔소리임?
# '''

# # 대결 대미지
# '''
# 기사가 밀리면 밀려난 기사는 피해를 입음. 함정의 수만큼만 피해를 입게 됨
# 체력 이상을 받으면 사라짐
# 명령을 받은 기사는 피해를 입지 않고, 기사들은 모두 밀린 이후에 대미지를 입게 됨
# 밀려도 그 위치에 함정이 없으면 피해 안 입는다. <<<<< 유의
# '''
# # 왕이 사라진 기사한테 명령할 수도 있으니 유의 



# from collections import deque

# L, N, Q = map(int,input().split())
# # 2로 둘러버리자
# board = [[2] * (L + 2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L + 2)]
# # 위 오른쪽 아래 왼쪽
# dr = [-1,0,1,0]
# dc = [0,1,0,-1]

# # 1 2 2 1 5
# knight_map = {}
# for i in range(1, N+1):
#     r, c, h, w, k = map(int, input().split())
#     knight_map[i] = (r, c, h, w, k) 
#     # 방패 범위랑, 기사 좌표랑 정보까지


# def is_live(i):
#     if i in knight_map and knight_map[i][4] > 0: 
#         return True
#     return False




# # 방패가 왜캐 커 
# def knight_move(i,d):
#     # 왕의 명령을 받아야함.
#     # 기사가 살아있는지부터 
#     if not is_live(i):
#         return
#     queue = deque([i])

#     trap_cnt = 0
#     while queue:
#         current_knight = queue.popleft()
#         cr, cc, ch, cw, ck = knight_map[current_knight]

        
#         # 결국엔 방패를 움직여야하니까 범위를 계산해야함...
#         for r in range(cr, cr + ch):
#             for c in range(cc, cc+ cw):
#                 nr = r + dr[d]
#                 nc = c + dc[d]

#                 if 0 <= nr < L+2 and 0 <= nc < L+2:
#                     for idx in range(1, len(knight_map)+1):
#                         if idx != current_knight:
#                             oor, oc, oh, ow, ok = knight_map[idx]
#                             if oor <= nr < oh + nr and oc <= nc < oc + ow:
#                                 queue.append(idx)

#                 if board[nr][nc] == 2:
#                     trap_cnt += 1

#         knight_map[current_knight] = (cr + dr[d], cc + dc[d], ch, cw, ck - trap_cnt)
#         if knight_map[current_knight][4] <= 0:
#             del knight_map[current_knight]

#     return trap_cnt

# queris = tuple(map(int, input().split()) for _ in range(Q))

# total = 0
# for i, d in queris:
#     total += knight_move(i, d)
# print(total) 
                

#     # i번째가 방패가 전부 d 방향으로 이동해야함 그러기 위해선 가는 길목에 범위를 넘어가거나 벽이면 안됨
#     # 그 전에 왕이 사라진 놈한테도 명령 가능하니까 이것도 처리해야함
        

# '''
# 왕의 명령을 받아서 i, d
# i번째 기사가 움직여야하는데 우선 해야할 것이
# i번째 기사가 살아있는지 확인하고
# is_live를 구현해서 
# 그리고 기사를 움직이기 기사가 (r,c)이고 방패가 [r:r+h][c:c+w]이니까 
# d 방향에서 방패를 [r+d:r+h+d][c+d:c+w+d] 이렇게 움직이여야하나?




# '''


from collections import deque

# L, N, Q = map(int,input().split())
# 2로 둘러싸서 체스판 생성
# board = [[2] * (L + 2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L + 2)]

# # 위 오른쪽 아래 왼쪽
# dr = [-1,0,1,0]
# dc = [0,1,0,-1]

# # 기사 정보 저장
# knights = {}
# for i in range(1, N + 1):
#     r, c, h, w, k = map(int, input().split())
#     knights[i] = (r, c, h, w, k)

# def is_valid_position(r, c):
#     return 1 <= r < L + 1 and 1 <= c < L + 1

# cnt = 0
# def move_knight(knight_id, d):
#     global cnt
#     if knight_id not in knights or knights[knight_id][4] <= 0:
#         return 0

#     r, c, h, w, k = knights[knight_id]
#     nr, nc = r + dr[d], c + dc[d]

#     # 미는 기사가 함정에 걸리는 경우 처리
#     for row in range(nr, nr + h):
#         for col in range(nc, nc + w):
#             if is_valid_position(row, col) and board[row][col] == 1:
#                 k -= 1
#                 cnt += 1

#     if k <= 0:
#         del knights[knight_id]
#         return 0 

#     # 이동 가능한지 확인
#     for other_id, (or_, oc, oh, ow, ok) in knights.items():
#         if other_id == knight_id:
#             continue
#         for row in range(or_, or_ + oh):
#             for col in range(oc, oc + ow):
#                 if nr <= row < nr + h and nc <= col < nc + w:
#                     trap_cnt = 0
#                     for r in range(or_ + dr[d], or_ + dr[d] + oh):
#                         for c in range(oc + dc[d], oc + dc[d] + ow):
#                             if is_valid_position(r, c) and board[r][c] == 1:
#                                 cnt += 1
#                                 trap_cnt += 1
#                     knights[other_id] = (or_ + dr[d], oc + dc[d], oh, ow, ok - trap_cnt)
#                     if knights[other_id][4] <= 0:
#                         del knights[other_id]
#                     move_knight(other_id, d) 
#     return cnt
    
# queries = tuple(map(int, input().split()) for _ in range(Q))
# total = 0
# for i, d in queries:
#     total += move_knight(i, d)
# print(total)




# def knight_move(i,d):
#     # 기사 이동 함수
#     if not is_live(i):
#         return False  # 기사가 살아있지 않으면 0 반환
#     queue = deque([i])

#     trap_cnt = 0 
#     while queue:
#         current_knight = queue.popleft()
#         cr, cc, ch, cw, ck = knight_map[current_knight]

#         for r in range(cr, cr + ch):
#             for c in range(cc, cc+ cw):
#                 nr = r + dr[d]
#                 nc = c + dc[d]

                
#                 if 1 <= nr < L+2 and 1 <= nc < L+2 and board[nr][nc] != 2:  
#                     for other_knight in knight_map:
                        
#                         if other_knight != current_knight:
#                             oor, oc, oh, ow, ok = knight_map[other_knight]
#                             for x in range(oor, oor+oh):
#                                 for y in range(oc, oc+ow):
#                                     nx = x + dr[d]
#                                     ny = y + dc[d]

#                                     if 1 <= nx < L+2 + oor and 1 <= ny < L+2:  
#                                         queue.append(other_knight)
#                                         if board[nx][ny] == 1:
#                                             trap_cnt += 1
                                    
                            

#                 # 함정 개수 세기, 밀려나 기사만 피해를 입음
#                 # 이건 미는 애가 함정에 걸리는거라 위에서 하나 더 구현해야한다.
                

       
#         knight_map[current_knight] = (cr + dr[d], cc + dc[d], ch, cw, ck - trap_cnt)
#         if knight_map[current_knight][4] <= 0:
#             del knight_map[current_knight]
#         #print(trap_cnt)
      
#     return trap_cnt 


# queries = tuple(map(int, input().split()) for _ in range(Q))

# total = 0
# for i, d in queries:
#     total += knight_move(i, d)  

# print(total) 



# 데미지는 초기값을 저장해놓자
L, N, Q = map(int,input().split())

di = [-1,0,1,0]
dj = [0,1,0,-1]
arr = [[2] * (L + 2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L + 2)]
units = {}
v = [[0] * (N+2) for _ in range(N+2)]
init_k =[0] * (N+1)
for m in range(1, N+1):
    si,sj,h,w,k = map(int, input().split())
    units[m] = [si,sj,h,w,k]
    init_k[m] = k
    for i in range(si, si+h):
        v[i][sj:sj+w] = [m]*w

def push_unit(start, dr): # s를 밀고, 연쇄처리 ... 
    q = []                 # push 후보 저장
    pset = set()            # 이동 기사번호 저장
    damage = [0]*(N+1)

    q.append(start)         # 초기데이터 append
    pset.add(start)

    while q:
        cur = q.pop(0) # q에서 데이터 꺼내기
        ci,cj,h,w,k = units[cur]

        # 명령받은 방향진행, 벽x, 겹치는 다른거면 q에 append
        ni,nj = ci+di[dr], cj+dj[dr]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j] == 2:  #  벽이면 
                    return
                if arr[i][j] == 1:
                    damage[cur] += 1 # 데미지 누적

        # 겹치는 다른 유닛있는 경우 q에 추가
        for idx in units:
            if idx in pset: continue # 이미 움직일 대상이면 

            ti,tj,th,tw,tk = units[idx]
            # 겹치는 경우
            if ni <= ti+th-1 and ni+h-1 >= ti and tj <= nj+w-1 and nj <= tj+tw-1:
                q.append(idx)
                pset.add(idx)

    # 명령 받은 기사는 데미지 입지 않음
    damage[start] = 0
    # 이동, 데미지 체력이상이면 제거
    for idx in pset:
        si, sj, h, w, k = units[idx]

        if k <= damage[idx]: # 체력보다 더 큰 데미지면 삭제
            units.pop(idx)
        else:
            ni, nj = si+di[dr], sj+dj[dr]
            units[idx] = [ni,nj,h,w,k-damage[idx]]

for _ in range(Q):
    idx, dr = map(int,input().split())
    if idx in units:
        push_unit(idx, dr) # 명령받은 기사(연쇄적으로 밀기: 벽이 없는 경우까지)


ans = 0
for idx in units:
    ans += init_k[idx] - units[idx][4]
print(ans)