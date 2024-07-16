n, m = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(n)]


def ractang():
    result = 0
    for i in range(n-1):
        for j in range(n-1):
            ract_sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            real_sum = ract_sum - min(matrix[i][j] , matrix[i][j+1] , matrix[i+1][j] , matrix[i+1][j+1])
            result = max(result, real_sum)
    return result


def strat_row():
    row_sum = []
    # 행 다 더하기
    for row in range(n):
        row_sum.append(sum(matrix[row]))
       # print(matrix[row])
    return max(row_sum)

def strat_col():
    col_sum = []
    for i in range(n):
        col_sub = []
        for j in range(n):
            col_sub.append(matrix[j][i])
        col_sum.append(sum(col_sub))

    return max(col_sum)

print(max(ractang(),strat_row(), strat_col()))