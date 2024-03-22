from collections import deque

def left(n, d):
    if n < 0:
        return

    if gears[n][2] != gears[n+1][6]:
        left(n-1, -d)
        gears[n].rotate(d)

def right(n, d):
    if n > 3:
        return
    if gears[n-1][2] != gears[n][6]:
        right(n+1, d)
        gears[n].rotate(d)

def calculate_score():
    score = 0
    for i, gear in enumerate(gears):
        if gear[0] == '1':
            score += 2**i
    return score

gears = [deque(input()) for _ in range(4)]
k = int(input())

for _ in range(k):
    n, d = map(int ,input().split())
    n -= 1

    left(n-1, -d)
    right(n+1, -d)
    gears[n].rotate(d)

print(calculate_score())