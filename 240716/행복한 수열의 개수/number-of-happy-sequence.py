n, m = map(int,input().split())

series_map = [list(map(int,input().split())) for _ in range(n)]


happy = 0

def check_happy(arr):
    cnt = 1
    max_cnt = 1
    for k in range(1, len(arr)):
        if arr[k] == arr[k-1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    max_cnt = max(max_cnt, cnt)
    return max_cnt >= m

for i in range(n):
    row_happy = check_happy(series_map[i])
    col_haapy = check_happy([series_map[j][i] for j in range(n)])

    if row_happy:
        happy += 1
    if col_haapy:
        happy += 1

print(happy)