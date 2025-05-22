# n = int(input())
# commands = [tuple(input().split()) for _ in range(n)]
# x = []
# dir = []
# for num, direction in commands:
#     x.append(int(num))
#     dir.append(direction)

# # Please write your code here.
# offset = 1000*100
# points = [[0,0] for _ in range(offset*2)]
# maps = [""] * offset * 2
# #points 가 2가 되면 회색
# # L => 흰색, R => 검은색
# temp_point = offset

# for i in range(n):
#     if dir[i] == "R":
#         for j in range(temp_point, temp_point + x[i] + 1):
#             points[j][0] += 1
#             if points[j][0] >= 2 and points[j][1] >= 2:
#                 maps[j] = "G"
#             else :
#                 maps[j] = "B"
#         temp_point = temp_point + x[i]
#     else:
#         for j in range(temp_point, temp_point - x[i] - 1, -1):
#             points[j][1] += 1
#             if points[j][0] >= 2 and points[j][1] >= 2:
#                 maps[j] = "G"
#             else :
#                 maps[j] = "W"
#         temp_point = temp_point - x[i]


#             #흰, 검, 회
# color_list = [0, 0, 0]

# for e in maps:
#     if e == "W":
#         color_list[0] += 1
#     elif e == "B":
#         color_list[1] += 1
#     elif e == "G":
#         color_list[2] += 1


# for e in color_list:
#     print(e, end = " ")

# print(maps[offset-10: offset+11])
# print(points[offset-10: offset+11])
# print(x)
# print(dir)

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

offset = 1000 * 100
points = [[0, 0] for _ in range(offset * 2)]
maps = [""] * (offset * 2)
temp_point = offset

for i in range(n):
    if dir[i] == "R":
        for j in range(1, x[i] + 1):  # 현재 위치는 제외, 다음 칸부터 x칸
            temp_point += 1
            points[temp_point][0] += 1
            if points[temp_point][0] >= 1 and points[temp_point][1] >= 1:
                maps[temp_point] = "G"
            else:
                maps[temp_point] = "B"
    else:  # "L"
        for j in range(1, x[i] + 1):  # 현재 위치는 제외
            temp_point -= 1
            points[temp_point][1] += 1
            if points[temp_point][0] >= 1 and points[temp_point][1] >= 1:
                maps[temp_point] = "G"
            else:
                maps[temp_point] = "W"

# 색상 개수 세기
color_list = [0, 0, 0]  # W, B, G

for color in maps:
    if color == "W":
        color_list[0] += 1
    elif color == "B":
        color_list[1] += 1
    elif color == "G":
        color_list[2] += 1

print(*color_list)
