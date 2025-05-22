x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split()) #a
x1[1], y1[1], x2[1], y2[1] = map(int, input().split()) #b
x1[2], y1[2], x2[2], y2[2] = map(int, input().split()) #m

# Please write your code here.
#전체 구하고, a, b 구하고(2됨) , m을 추가로 넣어서 2인 수치만 계산

OFFSET = 1000
maps = [[0] * OFFSET * 2 for _ in range(OFFSET*2)]

#a,b를 포함하는 최소한의 직사각형
#x 최소 최대, y 최소 최대
min_x = min(x1[0], x1[1])
max_x = max(x2[0], x2[1])
min_y = min(y1[0], y1[1])
max_y = max(y2[0], y2[1])

for i in range(min_x + OFFSET, max_x + OFFSET):
    for j in range(min_y + OFFSET, max_y + OFFSET):
        maps[i][j] = 1

#a,b 넓이 구하기
#a
for i in range(x1[0] + OFFSET, x2[0]+ OFFSET):
    for j in range(y1[0]+ OFFSET, y2[0]+ OFFSET):
        maps[i][j] = 2

#b
for i in range(x1[1]+ OFFSET, x2[1]+ OFFSET):
    for j in range(y1[1]+ OFFSET, y2[1]+ OFFSET):
        maps[i][j] = 2

#m 넓이 구하기
for i in range(x1[2]+ OFFSET, x2[2]+ OFFSET):
    for j in range(y1[2]+ OFFSET, y2[2]+ OFFSET):
        maps[i][j] = 3

# maps[][] = 2 구하기
result = 0
for row in maps:
    for cell in row:
        if cell == 2:
            result += 1

print(result)