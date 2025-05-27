N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
#    동 서 남 북 
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dir_string = {
    "E" : 0,
    "W" : 1,
    "S" : 2,
    "N" : 3,
}

# dir_num = dir_string[dir[0]] # 3

OFFSET = 10*100
SIZE = OFFSET * 2
arr = [[-1] * SIZE for _ in range(SIZE)]
arr[OFFSET][OFFSET] = 0
y = OFFSET
x = OFFSET
dir_num = 0
result = -1
cnt = 0

def in_range(x,y):
    return 0 <= x < SIZE and 0 <= y < SIZE

for i in range(N):
    for j in range(dist[i]):
        dir_num = dir_string[dir[i]]
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        cnt += 1
        if in_range(nx, ny) and (ny != 1000 or nx != 1000):
            x = x + dx[dir_num]
            y = y + dy[dir_num]
            arr[y][x] = cnt

        elif in_range(nx, ny) and ny == 1000 and nx == 1000:
            result = cnt
            break
    if(result == cnt):
        break


print(result)
        


    
