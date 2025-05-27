n, m = map(int, input().split())

# Please write your code here.
#     하 우 상 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [[0] * m for _ in range(n)]
dir_num = 0
cnt = 1
arr[0][0] = cnt
x,y = 0, 0

def in_range(x,y):
    return 0 <= x < m and 0 <= y < n

for i in range(2, n * m + 1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    cnt += 1
    if in_range(nx, ny) and arr[ny][nx] == 0:
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        arr[y][x] = cnt
    else :
        dir_num = (dir_num +1) % 4
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        arr[y][x] = cnt

for row in arr:
    for cell in row:
        print(cell, end = " ")
    print()

