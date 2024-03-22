n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


def calc_score(team):
    score = 0
    for i in team:
        for j in team:
            if i != j:
                score += matrix[i][j]
    return score


def dfs(start, team):
    global ans
    if len(team) == n // 2:
        other_team = [x for x in range(n) if x not in team]
        diff = abs(calc_score(team) - calc_score(other_team))
        ans = min(ans, diff)
        return
    
    for i in range(start, n):
        team.append(i)
        dfs(i + 1, team)
        team.pop()

ans = float('inf')
dfs(0, [])
print(ans)