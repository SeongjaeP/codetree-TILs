#행의 개수가 열의 개수보다 크거나 같은 경우 33 32
'''
1. 빈도 수가 적은 순서대로로 오름차순
2. 빈도가 같으면 수가 작은거로 오름차순
3. 숫자와 해당 숫자의 출현 빈도 수를 함께 출력
'''

# 행의 개수가 열의 개수보다 작은경우
'''
모든 열에 위의 과정 수행
'''

# 행이나 열의 길이가 100을 넘어가면 처음 100개 제외하고 버리기 [:100]
from collections import Counter

r, c, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(3)]


def based_row(matrix):
    
    new_matrix = []
    for row in matrix:
        
        new_row = []
        ex_counter = Counter(row)
        sorted_counter = sorted(ex_counter.items(), key=lambda x: (-x[1], x[0]))
        for item, count in sorted_counter:
            new_row.extend([item, count])
        new_matrix.append(new_row)
            
    lengths = [len(row) for row in new_matrix]
    max_length = max(lengths)
    for row in new_matrix:
        while len(row) < max_length:
            row.append(0)
        
    return new_matrix


def based_column(matrix):
    
    columns = [ [row[i] for row in matrix] for i in range(len(matrix[0]))]
    new_columns = []

    for col in columns:
        ex_counter = Counter(col)
        sorted_counter = sorted(ex_counter.items(), key=lambda x: (-x[1], x[0]))
        new_col = []
        for item, count in sorted_counter:
            new_col.extend([item, count])
        new_columns.append(new_col)

    max_length = max(len(col) for col in new_columns)

    for col in new_columns:
        while len(col) < max_length:
            col.append(0)
    
    transposed_columns_matrix = list(zip(*new_columns))
    
    return transposed_columns_matrix

i = 0
while True:
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        if board[r-1][c-1] == k:
            print(i)
            break
    if i > 100:
        print(-1)
        break

    else:
        if len(board) > 100:
            board = board[:100]

        if len(board[0]) > 100:
            board = [row[:100] for row in board]

        if len(board) >= len(board[0]):
            board = based_row(board) 
           
        elif len(board) < len(board[0]):
            board = based_column(board) 
        
        i += 1
    
else:  
    print(-1)