N = int(input())

num_list = [list(map(int, input().split())) for _ in range(N)]

now_coin = 0
max_coin = 0
for row in range(N-2):
    for col in range(N-2):
        now_coin = sum(num_list[row][col:col+3]) + sum(num_list[row+1][col:col+3]) + sum(num_list[row+2][col:col+3])
        max_coin = max(now_coin, max_coin)

print(max_coin)