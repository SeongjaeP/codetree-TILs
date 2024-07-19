n, t = map(int, input().split())
num_map = [list(map(int, input().split())) for _ in range(3)]

for _ in range(t):
    temp = [num_map[i][-1] for i in range(3)]
   
    for i in range(3):
        if i == 0:
            num_map[i] = [temp[2]] + num_map[i][:-1]
        else:
            num_map[i] = [temp[i-1]] + num_map[i][:-1]

for row in num_map:
    print(" ".join(map(str, row)))