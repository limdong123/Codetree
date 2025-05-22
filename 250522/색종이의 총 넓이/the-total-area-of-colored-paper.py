n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
#x ~ x+8 
OFFSET = 100
maps = [[0]*OFFSET*2 for _ in range(OFFSET*2)]

for i in range(n):
    for j in range(x[i] + OFFSET, x[i] + 8+ OFFSET):
        for k in range(y[i]+ OFFSET, y[i] + 8+ OFFSET):
            maps[j][k] = 1

result = 0
for row in maps:
    for cell in row:
        if cell == 1:
            result += 1

print(result)