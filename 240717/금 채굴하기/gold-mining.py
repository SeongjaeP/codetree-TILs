# 완전 탐색
# n, m = map(int,input().split())

# gold_map = [list(map(int,input().split())) for _ in range(n)]
# # k = 1


# def cnt_gold(row,col,k):
#     gold = 0
#     for i in range(n):
#         for j in range(n):
#             if abs(row-i) + abs(col-j) <= k:
#                 gold += gold_map[i][j]
#     return gold

# def cost_gold(k):
#     return k*k + (k+1)*(k+1)

# max_gold = 0

# for row in range(n):
#     for col in range(n):
#         for k in range(2 * (n-1) + 1):
#             num_of_gold = cnt_gold(row, col, k)

#             if num_of_gold * m >= cost_gold(k):
#                 max_gold = max(max_gold, num_of_gold)


# print(max_gold)


# DP
n, m = map(int, input().split())

gold_map = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = gold_map[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

def sum_region(x1, y1, x2, y2):
    x1, y1, x2, y2 = max(0, x1), max(0, y1), min(n, x2), min(n, y2)
    return prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]

def cnt_gold(row, col, k):
    total_gold = 0
    for i in range(max(0, row - k), min(n, row + k + 1)):
        for j in range(max(0, col - k), min(n, col + k + 1)):
            if abs(row - i) + abs(col - j) <= k:
                total_gold += gold_map[i][j]
    return total_gold

def cost_gold(k):
    return k * k + (k + 1) * (k + 1)

max_gold = 0

for row in range(n):
    for col in range(n):
        k = 0
        while k < 2 * (n - 1) + 1:
            num_of_gold = cnt_gold(row, col, k)
            if num_of_gold * m >= cost_gold(k):
                max_gold = max(max_gold, num_of_gold)
            k += 1

print(max_gold)