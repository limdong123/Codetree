n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
#0,3 - 1,2    ---- 3-n 반대로 진행 

#    상, 우, 좌, 하
dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]


dirs = {
    "U" : 0,
    "D" : 3,
    "R" : 1,
    "L" : 2
}
#초기 방향
move_dir = dirs[d]

# R -> 행, C -> 열
ny, nx = r - 1, c - 1

def in_range(x,y) :
    return 0 <= x < n and 0 <= y < n

# 벽에 부딧치면 방향 바꾸는데 1초 소요
for i in range(t):
    nx = nx + dx[move_dir]
    ny = ny + dy[move_dir]
    if not in_range(nx, ny) : #벽에 부딧치면 방향 전환, 좌표는 그대로
        nx = nx - dx[move_dir]
        ny = ny - dy[move_dir]
        move_dir = 3 - move_dir    


print(ny + 1, nx + 1)

                
        

