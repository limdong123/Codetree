x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
# 처음[0] 직사각형 넓이 배열에 1로 바꾸기 => 두번째 직사각형 배열 0으로 바꾸기 
# => 이후 1이 나오는 값 x 의 최솟값 최댓값, y 최솟값, 최댓값으로 직사각형 최소 넓이 구하기
OFFSET = 1000
size = OFFSET * 2
maps = [[0] * size for _ in range(size)]

for i in range(x1[0] + OFFSET, x2[0] + OFFSET +1):
    for j in range(y1[0] + OFFSET, y2[0] + OFFSET +1):
        maps[i][j] = 1

for i in range(x1[1] + OFFSET, x2[1] + OFFSET + 1):
    for j in range(y1[1] + OFFSET, y2[1] + OFFSET+ 1):
        maps[i][j] = 0


min_x, max_x, min_y, max_y = 2001, 0, 2001, 0

for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == 1:
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

print((max_x - min_x) * (max_y - min_y))
