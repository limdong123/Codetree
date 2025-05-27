n, m = map(int, input().split())

# Please write your code here.
ap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"
, "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#    우 하 좌 상      
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

arr = [[""] * m for _ in range(n)]
dir_num = 0
x,y = 0, 0
cnt = 0
arr[y][x] = ap[cnt]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

for i in range(2, n * m + 1):
    cnt += 1
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    
    if in_range(nx, ny) and arr[ny][nx] == "":
        x = nx 
        y = ny 
        arr[y][x] = ap[(cnt % 26)]
    else :
        dir_num = (dir_num + 1 ) % 4
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        arr[y][x] = ap[(cnt % 26)]

for row in arr:
    for cell in row:
        print(cell, end = " ")
    print()