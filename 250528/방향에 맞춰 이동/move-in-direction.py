n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# w,s,n,e = 서(-1,0), 남(0, -1), 북(0,1), 동(1,0)
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
di = ["W", "S", "N", "E"]

nx, ny = 0, 0
for i in range(n):
    if dir[i] == "W":
        nx += dx[0] * dist[i] 
        ny += dy[0] * dist[i]
    elif dir[i] == "S":
        nx += dx[1] * dist[i] 
        ny += dy[1] * dist[i]
    elif dir[i] == "N":
        nx += dx[2] * dist[i] 
        ny += dy[2] * dist[i]
    elif dir[i] == "E":
        nx += dx[3] * dist[i] 
        ny += dy[3] * dist[i]
    
print(nx, ny)


# print(dir) ['N', 'E', 'S', 'E']
# print(dist) [3, 2, 1, 2] 
