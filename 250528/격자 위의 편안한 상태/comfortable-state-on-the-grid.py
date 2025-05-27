n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
#    상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#색 칠하고 사방탐색해서 3칸 이상 칠했으면 1출력
arr = [[0] * (n) for _ in range(n)]
x,y = 0, 0

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

for i in range(m):
    y = points[i][0] -1
    x = points[i][1] -1
    arr[y][x] = 1
    cnt = 0
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if in_range(nx, ny) and arr[ny][nx] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else :
        print(0)
