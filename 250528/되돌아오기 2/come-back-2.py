commands = input()

# Please write your code here.
#    상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

y, x = 0, 0
cnt = 0
dir_num = 0 
result = -1

for i in commands:
    cnt += 1
    if i == "F":
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        if x == 0 and y == 0:
            result = cnt
            break
    elif i == "R":
        dir_num = (dir_num + 1) % 4
    elif i == "L":
        dir_num = (dir_num -1 + 4) % 4

print(result)
        
