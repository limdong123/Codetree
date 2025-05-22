n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
offset = 1000*100
points = [[0,0] for _ in range(offset*2)]
maps = [""] * offset * 2
#points 가 2가 되면 회색
# L => 흰색, R => 검은색
temp_point = offset

for i in range(n):
    if dir[i] == "R":
        for j in range(temp_point, temp_point + x[i]):
            points[j][0] += 1
            if points[j][0] >= 2 and points[j][1] >= 2:
                maps[j] = "G"
            else :
                maps[j] = "B"
        temp_point +=  x[i] - 1
    else:
        for j in range(temp_point, temp_point - x[i], -1):
            points[j][1] += 1
            if points[j][0] >= 2 and points[j][1] >= 2:
                maps[j] = "G"
            else :
                maps[j] = "W"
        temp_point -=  x[i] + 1


            #흰, 검, 회
color_list = [0, 0, 0]

for e in maps:
    if e == "W":
        color_list[0] += 1
    elif e == "B":
        color_list[1] += 1
    elif e == "G":
        color_list[2] += 1


for e in color_list:
    print(e, end = " ")

