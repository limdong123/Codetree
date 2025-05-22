n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
OFFSET =  100
area = [[0] * OFFSET * 2 for _ in range(OFFSET * 2)]

for i in range(n):
    for j in range(x1[i] + OFFSET, x2[i] + OFFSET):
        for k in range(y1[i]+OFFSET, y2[i]+OFFSET):
            area[k][j] += 1

result = 0

for row in area:
    for cell in row:
        if cell >= 1:
            result += 1

print(result)