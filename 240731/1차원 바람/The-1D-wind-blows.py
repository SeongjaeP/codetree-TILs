shiftRight = 0
shiftLeft = 1
 
n, m, q = map(int, input().split())
building = [[0] * (m+1) for _ in range(n+1)]
    
def shift(row, currDir):
    if currDir == shiftRight:
        
        building[row].insert(1, building[row].pop())
    else:
        building[row].insert(m, building[row].pop(1))
 
    
def isSameNumber(row1, row2):
    return any([
        building[row1][col] == building[row2][col]
        for col in range(1, m + 1)
    ])
 
def flip(currDir):
    return shiftRight if currDir == shiftLeft else shiftLeft
 
def simulate(startRow, startDir):
    shift(startRow, startDir)
    startDir = flip(startDir)
 
    currDir = startDir
    for row in range(startRow, 1, -1):
        if isSameNumber(row, row - 1):
            shift(row - 1, currDir)
            currDir = flip(currDir)
        else:
            break
    
    currDir = startDir
    for row in range(startRow, n):
        if isSameNumber(row, row + 1):
            shift(row + 1, currDir)
            currDir = flip(currDir)
        else:
            break
 
        
for row in range(1, n + 1):
    givenNumber = list(map(int, input().split()))
    for col, num in enumerate(givenNumber, start = 1):
        building[row][col] = num
 
for _ in range(q):
    r, d = tuple(input().split())
    r = int(r)
 
    simulate(r, shiftRight if d == 'L' else shiftLeft)
 
for row in range(1, n + 1):
    for col in range(1, m + 1):
        print(building[row][col], end = " ")
    print()