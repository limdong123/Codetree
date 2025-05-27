n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
#    우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dir_num = 0 # 우 하 좌 상 증가 
y,x = 0, 0 
arr[y][x] = 1 # 초기값

def in_range(x,y):
    return 0 <= x < m and 0 <= y < n

for i in range(2, n * m + 1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not in_range(nx, ny) or arr[ny][nx] != 0 :
        dir_num = (dir_num +1) % 4
    
    x,y = x + dx[dir_num], y + dy[dir_num]
    arr[y][x] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()
