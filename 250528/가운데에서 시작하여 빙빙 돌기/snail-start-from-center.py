n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
#     우 상 좌 하 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_num = 0
x,y = n // 2, n // 2
arr = [[0] * n for _ in range(n)]
cnt = 1
arr[y][x] = cnt
 
def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


# 1 -> 1 -> 2-> 2-> 3-> 3 -> 4 -> 4-> 5->
# step = i // 2
step = 1
for i in range(2, n * n + 1):
    step = i // 2
    for _ in range(step): # step만큼 전진
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        if in_range(x, y) :
            cnt += 1
            arr[y][x] = cnt
    #전진 끝나면 방향 전환 
    dir_num = (dir_num + 1 ) % 4


    


for row in arr:
    for cell in row:
        print(cell, end = " ")
    print()
    
