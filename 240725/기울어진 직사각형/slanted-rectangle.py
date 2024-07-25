# 어려워서 해설 참고했습니다.. 

n = int(input())
board_map = [list(map(int,input().split())) for _ in range(n)]


dx = [1, -1, -1, 1]
dy = [-1, -1, 1, 1]

# 시작점 정하기
# 맨아래, 그 위 여기서 출발해야 가장 큰 값 얻을 수 있음.
# ㄴㄴ 완탐으로 해야해서 정하면 안됨. -> 위의 경우는 최대를 안 지나칠 수도 있다.


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def get_score(x, y, k, l):
    dxs = [1, -1, -1, 1]
    dys = [-1, -1, 1, 1] 
    move_nums = [k, l, k, l]

    sum_of_nums = 0

    # 기울어진 직사각형 경계 따라가기 
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy

            # 경계 벗어나거나
            # 불가능하면 0으로 반환
            if not in_range(x, y):
                return 0
            sum_of_nums += board_map[x][y]

    return sum_of_nums

ans = 0

# k, l을 선언하고, 다 훑어야한다. [k,l,k,l] 하는 이유는 돌아와야하니까,,

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_score(i, j, k, l))



print(ans)