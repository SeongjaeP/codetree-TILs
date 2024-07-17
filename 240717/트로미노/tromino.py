n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def max_rectangle_sum(matrix):
    max_sum = 0
    for i in range(n-1):
        for j in range(m-1):
            sub_matrix = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
            rect_sum = sum(sub_matrix) - min(sub_matrix)
            max_sum = max(max_sum, rect_sum)
    return max_sum

def max_row_sum(matrix):
    max_sum = 0
    for row in matrix:
        for i in range(m-2):
            row_sum = row[i] + row[i+1] + row[i+2]
            max_sum = max(max_sum, row_sum)
    return max_sum

def max_col_sum(matrix):
    max_sum = 0
    for j in range(m):
        for i in range(n-2):
            col_sum = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j]
            max_sum = max(max_sum, col_sum)
    return max_sum

print(max(max_rectangle_sum(matrix), max_row_sum(matrix), max_col_sum(matrix)))