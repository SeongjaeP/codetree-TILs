n, m = map(int,input().split())

gold_map = [list(map(int,input().split())) for _ in range(n)]
# k = 1


def cnt_gold(row,col,k):
    gold = 0
    for i in range(n):
        for j in range(n):
            if abs(row-i) + abs(col-j) <= k:
                gold += gold_map[i][j]
    return gold

def cost_gold(k):
    return k*k + (k+1)*(k+1)

max_gold = 0

for row in range(n):
    for col in range(n):
        for k in range(2 * (n-1) + 1):
            num_of_gold = cnt_gold(row, col, k)

            if num_of_gold * m >= cost_gold(k):
                max_gold = max(max_gold, num_of_gold)


print(max_gold)