N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.


#북쪽방향 시작 R -> 오른쪽 L 왼쪽 , F 전진
#    북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dir_num = 0

#중앙에서 시작
x = N // 2
y = N // 2

#처음 숫자 더해줘야함
sum = board[y][x]

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

for ch in str:
    if ch == "F":
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx, ny):
            x = nx
            y = ny
            sum += board[y][x]
    elif ch == "R":
        dir_num = (dir_num + 1 ) % 4
    elif ch == "L":
        dir_num = (dir_num -1 + 4) % 4

print(sum)

