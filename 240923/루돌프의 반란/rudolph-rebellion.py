# '''
# 좌상단은 (1,1)임 

# 루돌프 한번에 산타 1~P까지 순서대로 움직임. 기절해있거나 격자 ㅂ밖으로 빠져나갔으면 탈락이므로 못 움직임
# 두 칸의 거리는 뉴클리드 기하에 따름
# '''

# #루돌프
# ''' 
# 가까운 산타한테 1칸 돌진

# 가까운 산타가 2명이상이면 r좌표가 큰 산타를 향해 돌진. r도 동일하면 c 좌표가 큰 산타를 향해 돌진

# 루돌프는 상하좌우, 대각선을 포함한 인접한 8방향 중 하나로 돌진 가능. 가까워지는 방향으로 한 칸 돌진
# '''

# #산타 움직임
# '''
# 1~P까지 순서대로 움직
# 기절하면 탈락
# 산타또한 루돌프에게 가까워지게 1칸 움직임
# 산타 있는 칸으로 못감. 밖으로도 if 안에 있어야 하며 and 산타 있는 좌표값(ex 1) != 1
# 움직일 수 없으면 움직x(어떤 경우지?)

# 산타는 상화좌우 가능. 가까워질 수 있는 방향이 여러 개라면 상우하좌 우선순위임

# '''


# #충돌
# '''
# 산타 루돌프 같은 칸이면 충돌
# 루돌프 move -> 산타는C점수 얻게 됨 -> 루돌프 방향으로 C칸 만큼 밀려남(그대로 밀림)

# 산타 move -> 산타는D만큼의 점수 얻게 됨 -> 반대방향으로 D (팅겨남)

# 포물선으로 밀려남 -> 충돌 안함 -> 상호작용은 가능
# '''


# #상호작용
# '''
# 충돌한 밀렸을 때만 상호작용 가능
# 한칸씩 밀림 
# '''

# #기절
# '''
# 산타가 루돌프와 충돌하면 기절
# k번째 턴이었다면 k+1까지 기절 -> k+2번째 턴부터 다시 정상상태로 됨
# 기절한 산타 못 움직. 단 충돌이나 상호작용으로 인해 밀려날 수는 있음
# 루돌프도 기절한 산타를 돌진 대상으로 선택가능
# '''

# # 게임 종료
# '''
# M번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 이후 게임 종료
# P명이 산타가 모두 탈락이면 즉시 게임 종료
# 매 턴 이후 아직 탈락하지 않으면 1점 씩 추가로 부여
# '''

# N, M, P, C, D = map(int, input().split())
# Rr, Rc = map(int,input().split())

# drr = [0,0,1,-1,1,1,-1,-1]
# drc = [1,-1,0,0,1,-1,1,-1]

# dsr = [0,0,1,-1]
# dsc = [1,-1,0,0]
# # 기절

# def sleep():
#     # 산타랑 루돌프가 같은 위치 
#     if santa == rudolf:
#         santa = 1  # 언제 기절했는지 인덱스 추가

# def rudolf_move(santa_map):
#     distance =  [((Rr-Sr)**2 + (Rc-Sc)**2, Sr, Sc) for (Sr,Sc) in santa_map]
#     distance.sort(key=lambda x: (x[0], x[1], x[2]))
    
#     # 가장 가까워지는 방향
#     # distance = [(3, 2, 2), (5, )]
#     # ru = (5, 4)
#     if distance[0][1] != Rr and distance[0][2] != Rc:
#         # 
#     nr = Rr + dr
#     nc = Rc + dc

#     # 루돌프가 박치기를 하면
#     if nr == Sr and nc = Sc:
#         #  해당 산타 C만큼 점수 주고
#         Santa_n += C
#         if 



# def santa_move(santa_map):
    
#     distance = 
#     for Pn in santa_map:
#         # 기절이거나 and 
#         if not sleep() and 0 <= Pn[0] < N and 0 <= Pn[1] < N and santa_map != 1:


# # 루돌프가 박치기 
# def colld_rudolf():
#     # 해당 산타 C만큼 점수 얻고
#     santa_n += C
#     # 루돌프 이동 방향 가져와야함 -> move랑 하나로 움직여야한다


# # 산타가 박치기
# def colld_santa():
#     return 


# # rudolf_move
# # colld
# # interaction
# # santa_move
# # colld
# # interaction






def cal_dist(r1, c1, r2, c2):
    return abs(r1 - r2) ** 2 + abs(c1 - c2) ** 2


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx=[-1,-1,0,1,1, 1, 0,-1]
dy=[0 ,1 ,1,1,0,-1,-1,-1]
def roodolf_move(rounds):
    # 가장가까운 산타를 향해 1칸 돌진.
    # 산타가 둘이상이면 r좌표큰, 동일하면 c좌표큰
    # 상하좌우,대각선 포함해서 8방향.
    global rr,rc
    min_dist = 100000
    mr,mc = 10000,10000
    mnum= -1
    #산타 값 전부조회
    for num in range(1,p+1):
        sr,sc = s_where[num]
        if sr == -100 : continue
        dist = cal_dist(sr,sc,rr,rc)
        if (min_dist,-mr,-mc) >= (dist,-sr,-sc) : # 여기서 오류나면 그냥 for문으로 2차원배열 탐색으로 하기
            min_dist = dist 
            mr,mc = sr,sc
            mnum = num
    #print(mr,mc,mnum)

    r_dist = cal_dist(mr,mc,rr,rc)

    for dnum in range(8):
        nx,ny = rr+dx[dnum],rc+dy[dnum]
        n_dist = cal_dist(mr,mc,nx,ny)
        if in_range(nx,ny) and r_dist > n_dist :
            r_dist = n_dist
            nr,nc = nx,ny
            r_num = dnum

    #맵 갱신
    r_map[rr][rc] = 0
    r_map[nr][nc] = 1
    rr,rc = nr,nc
    # 박치기 충돌 구현해야함

    if s_map[rr][rc] != 0 :
        #누군가있다면
        santa = s_map[rr][rc]
        sx,sy = rr,rc
        #기절구현 주의
        break_santa[santa] = rounds + 2
        #점수구현
        s_point[santa] += c
        s_map[rr][rc] = 0
        #밀려나기 구현
        nnx,nny = sx+c*dx[r_num],sy+c*dy[r_num]
        if in_range(nnx,nny): # 밖으로 안 나갈때
            #만약에 밀려난곳에 산타가 있나 체크해야함
            s_where[santa] = nnx,nny
            mnumber = santa
            while True :
                if no_santa(nnx,nny) : break
                nnx,nny,mnumber = push(nnx,nny,mnumber,r_num)
            # 빠져나오고난다음 mnx,mny 에 자리 넣어줘야함.
            if in_range(nnx,nny): # 안쪽이면 반영해주기
                s_map[nnx][nny] = mnumber
                s_where[mnumber] = nnx,nny
            else : #밀려서 밖으로 나가면 우주로 ㅂㅂ
                s_where[mnumber] = -100,-100
        else :
            s_map[sx][sy] = 0
            s_where[santa] = -100, -100
            return

    return

def one_san_move(santa,rounds):
    if not break_santa[santa] <= rounds : return
    sx,sy = s_where[santa]
    if sx == -100 : return
    #루돌프에게 가까워지는 방향으로 1칸
    # 다른산타, 게임판밖 x
    # 움직못하면 그냥 가만히
    # 가까워지지 못하면 그냥 가만히
    s_dist = cal_dist(sx,sy,rr,rc)
    mx,my = sx,sy
    for num in range(0,8,2):
        nx,ny = sx+dx[num],sy+dy[num]
        n_dist = cal_dist(nx,ny,rr,rc)
        if in_range(nx,ny) and s_map[nx][ny] == 0 and  s_dist > n_dist : #상우하좌
            s_dist = n_dist
            mx,my = nx,ny
            mnum = num

    # 갱신 및 그림 업데이트
    s_map[sx][sy] = 0
    s_where[santa] = mx,my
    s_map[mx][my] = santa
    # 루돌프와 부딫힘 체크
    if rr == mx and rc == my: #밀려나야함
        # 점수얻기
        # d 거리만큼 튕겨나가기
        s_map[mx][my] = 0
        r_num = (mnum+4)%8
        #기절처리 주의
        break_santa[santa] = rounds + 2
        #포인트 처리
        s_point[santa] += d
        mnx,mny = mx+d*dx[r_num],my+d*dy[r_num]
        if in_range(mnx,mny): # 밖으로 나갈때
            #만약에 밀려난곳에 산타가 있나 체크해야함
            s_where[santa] = mnx,mny
            mnumber = santa
            while True :
                if no_santa(mnx,mny) : break
                mnx,mny,mnumber = push(mnx,mny,mnumber,r_num)
            # 빠져나오고난다음 mnx,mny 에 자리 넣어줘야함.
            if in_range(mnx,mny): # 안쪽이면 반영해주기
                #print(mnx,mny,mnumber)
                s_map[mnx][mny] = mnumber
                s_where[mnumber] = mnx,mny
            else : #밀려서 밖으로 나가면 우주로 ㅂㅂ
                s_where[mnumber] = -100,-100
        else :
            s_map[mx][my] = 0
            s_where[santa] = -100, -100
            return

    return

def push(x,y,num,r_num):

    mnumber = s_map[x][y]
    s_where[num] = x,y
    s_map[x][y] = num
    mx,my = x+dx[r_num],y+dy[r_num]
    return mx,my,mnumber


def no_santa(mnx,mny):
    if not in_range(mnx,mny) : return True
    if s_map[mnx][mny] == 0 :
        return True
    return False

def santa_move(rounds):

    for santa in range(1,p+1):
        one_san_move(santa,rounds)
    return


n,m,p,c,d = map(int,input().split())
s_point = [0 for _ in range((1+p))]
s_where = [(-1,-1) for _ in range((1+p))]
rr,rc = map(int,input().split())
rr-=1
rc-=1
r_map = [ [ 0 for _ in range(n)] for _ in range(n)]
s_map = [ [ 0 for _ in range(n)] for _ in range(n)]
r_map[rr][rc] = 1
break_santa = [0 for _ in range((1+p))]
for pn in range(p):
    snum,sr,sc = map(int,input().split())
    s_where[snum] = (sr-1,sc-1)
    s_map[sr-1][sc-1] = snum

def look_maps():
    print('산타')
    for k in s_map:
        print(*k)
    print('루돌')
    for k1 in r_map:
        print(*k1)
    return

def output_santa_point():
    for num in range(1,p+1):
        print(s_point[num],end=' ')
    return


def santa_dead_check():
    count = 0
    for santa in range(1,p+1):
        sx,sy = s_where[santa]
        if sx == -100 :
            count += 1

    return count == p
def santa_point_up():

    for num in range(1,p+1):
        sx,sy = s_where[num]
        if sx == -100 : continue
        s_point[num] += 1
    return
for rounds in range(m):
    roodolf_move(rounds)
    #look_maps()
    if santa_dead_check(): break
    santa_move(rounds)
    #look_maps()
    if santa_dead_check(): break
    santa_point_up()

output_santa_point()