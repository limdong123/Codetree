dirs = input()

# Please write your code here.
#L 반시계, R 시계, F 바라보는 방향 한칸 이동

#    북, 동, 남, 서
#     0   1  2   3
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0 #초기 북쪽 방향

for i in dirs:
    if i == "L":
        dir_num = (dir_num - 1 + 4 ) % 4
    elif i == "R":
        dir_num = (dir_num + 1) % 4
    elif i == "F":
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)