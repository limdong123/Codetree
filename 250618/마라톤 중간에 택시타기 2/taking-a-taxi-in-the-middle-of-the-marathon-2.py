n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

min_range = 1000*1000*100

for i in range(1, n - 1):
    temp_points = points[:i] + points[i+1:]
    
    #거리 구하기
    total = 0
    for j in range(n-1 - 1):
        x1 = temp_points[j][0]
        y1 = temp_points[j][1]
        x2 = temp_points[j+1][0]
        y2 = temp_points[j+1][1]
        total += abs(x1 - x2) + abs(y1 - y2)
    
    min_range = min(min_range, total)

print(min_range)