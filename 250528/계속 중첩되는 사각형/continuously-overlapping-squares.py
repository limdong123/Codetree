n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
#  홀수[인덱스는 짝수] -> red = 1, 짝수[인덱스는 홀수] -> blue = 2

OFFSET = 100
size = OFFSET * 2 #200
maps = [[0] * size for _ in range(size)]

for i in range(n):
    for j in range(x1[i] + OFFSET, x2[i]+ OFFSET):
        for k in range(y1[i]+ OFFSET, y2[i]+ OFFSET):
            if i % 2 == 0: #red
                maps[j][k] = 1
            elif i % 2 == 1: #blue
                maps[j][k] = 2

result = 0
for row in maps:
    for cell in row:
        if cell == 2:
            result += 1


print(result)
