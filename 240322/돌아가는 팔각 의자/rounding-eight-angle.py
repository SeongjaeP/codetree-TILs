from collections import deque   

def left(gear_index, direction):
    if gear_index < 0: return

    if gears[gear_index][2] != gears[gear_index+1][6]:
        left(gear_index-1, -direction)
        gears[gear_index].rotate(direction)

def right(gear_index, direction):
    if gear_index > 3: return

    if gears[gear_index-1][2] != gears[gear_index][6]:
        right(gear_index+1, -direction)
        gears[gear_index].rotate(direction)

def calculate_score():
    score = 0
    for i, gear in enumerate(gears):
        if gear[0] == '1':
            score += 2**i
    return score

# 톱니바퀴 초기화
gears = [deque(input()) for _ in range(4)]

# 회전 횟수
k = int(input())

# 회전 실행
for _ in range(k):
    gear_index, direction = map(int, input().split())
    gear_index -= 1  # 인덱스 조정

    left(gear_index - 1, -direction)
    right(gear_index + 1, -direction)
    gears[gear_index].rotate(direction)

print(calculate_score())