class Game:
    DIR_NUM = 8
    P_DIR_NUM = 4
    MAX_DECAY = 2
    MAX_T = 25
    MAX_N = 4

    def __init__(self, n, m, t, px, py, monsters):
        self.n = n
        self.m = m
        self.t = t
        self.px = px - 1
        self.py = py - 1
        self.t_num = 1
        self.monster = [
            [
                [
                    [0] * Game.DIR_NUM
                    for _ in range(n)
                ]
                for _ in range(n)
            ]
            for _ in range(Game.MAX_T + 1)
        ]
        self.dead = [
            [
                [0] * (Game.MAX_DECAY + 1)
                for _ in range(n)
            ]
            for _ in range(n)
        ]

        for mx, my, mdir in monsters:
            self.monster[0][mx - 1][my - 1][mdir - 1] += 1

        self.dxs = [-1, -1,  0,  1, 1, 1, 0, -1]
        self.dys = [ 0, -1, -1, -1, 0, 1, 1,  1]
        self.p_dxs = [-1,  0, 1, 0]
        self.p_dys = [ 0, -1, 0, 1]

    def in_range(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def can_go(self, x, y):
        return self.in_range(x, y) and self.dead[x][y][0] == 0 and self.dead[x][y][1] == 0 \
           and (x, y) != (self.px, self.py)

    def get_next_pos(self, x, y, move_dir):
        for c_dir in range(Game.DIR_NUM):
            n_dir = (move_dir + c_dir + Game.DIR_NUM) % Game.DIR_NUM
            nx, ny = x + self.dxs[n_dir], y + self.dys[n_dir]
            if self.can_go(nx, ny):
                return nx, ny, n_dir
        return x, y, move_dir

    def move_m(self):
        for i in range(self.n):
            for j in range(self.n):
                for k in range(Game.DIR_NUM):
                    x, y, next_dir = self.get_next_pos(i, j, k)
                    self.monster[self.t_num][x][y][next_dir] += self.monster[self.t_num - 1][i][j][k]

    def get_killed_num(self, dir1, dir2, dir3):
        x, y = self.px, self.py
        killed_num = 0
        v_pos = []

        for move_dir in [dir1, dir2, dir3]:
            nx, ny = x + self.p_dxs[move_dir], y + self.p_dys[move_dir]
            if not self.in_range(nx, ny):
                return -1
            if (nx, ny) not in v_pos:
                killed_num += sum(self.monster[self.t_num][nx][ny])
                v_pos.append((nx, ny))
            x, y = nx, ny
        
        return killed_num

    def do_kill(self, best_route):
        dir1, dir2, dir3 = best_route
        for move_dir in [dir1, dir2, dir3]:
            nx, ny = self.px + self.p_dxs[move_dir], self.py + self.p_dys[move_dir]
            
            for i in range(Game.DIR_NUM):
                self.dead[nx][ny][Game.MAX_DECAY] += self.monster[self.t_num][nx][ny][i]
                self.monster[self.t_num][nx][ny][i] = 0
                
            self.px, self.py = nx, ny

    def move_p(self):
        max_cnt = -1
        best_route = (-1, -1, -1)

        for i in range(Game.P_DIR_NUM):
            for j in range(Game.P_DIR_NUM):
                for k in range(Game.P_DIR_NUM):
                    m_cnt = self.get_killed_num(i, j, k)
                    if m_cnt > max_cnt:
                        max_cnt = m_cnt
                        best_route = (i, j, k)
        
        self.do_kill(best_route)

    def decay_m(self):
        for i in range(self.n):
            for j in range(self.n):
                for k in range(Game.MAX_DECAY):
                    self.dead[i][j][k] = self.dead[i][j][k + 1]
                self.dead[i][j][Game.MAX_DECAY] = 0

    def add_m(self):
        for i in range(self.n):
            for j in range(self.n):
                for k in range(Game.DIR_NUM):
                    self.monster[self.t_num][i][j][k] += self.monster[self.t_num - 1][i][j][k]

    def simulate(self):
        self.move_m()
        self.move_p()
        self.decay_m()
        self.add_m()

    def count_monster(self):
        cnt = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(Game.DIR_NUM):
                    cnt += self.monster[self.t][i][j][k]
        return cnt

    def run(self):
        while self.t_num <= self.t:
            self.simulate()
            self.t_num += 1
        print(self.count_monster())

# 입력 부분
n = 4
m, t = map(int, input().split())
px, py = map(int, input().split())
monsters = [tuple(map(int, input().split())) for _ in range(m)]

game = Game(n, m, t, px, py, monsters)
game.run()