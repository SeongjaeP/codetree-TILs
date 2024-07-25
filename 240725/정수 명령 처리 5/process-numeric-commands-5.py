N = int(input())
dp = []

for _ in range(N):
    a = input()

    if a.split(' ')[0] == 'push_back':
        dp.append(a.split(' ')[1])
    if a.split(' ')[0] == 'get':
        print(dp[int(a.split(' ')[1]) - 1])
    if a == 'size':
        print(len(dp))
    if a.split(' ')[0] == 'pop_back':
        dp.pop()