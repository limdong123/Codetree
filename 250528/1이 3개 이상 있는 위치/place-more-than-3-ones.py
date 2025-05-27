n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#    상  우  하  좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def in_range(x,y): #범위 안에 들어가는지 안들어가는지 확인하는 함수
    return 0 <= x < n and 0 <= y < n

cnt = 0 #상하좌우 1이 3개 이상인 것
cnt_1 = 0
for y in range(n):
    for x in range(n):
        cnt_1 = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if in_range(nx, ny) and grid[ny][nx] == 1:
                cnt_1 += 1
        
        if cnt_1 >= 3:
            cnt += 1

print(cnt)