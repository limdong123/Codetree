n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

points = [0] * (200)

for i in range(n):
    for j in range(segments[i][0] + 100, segments[i][1] + 101):
        points[j] += 1

result = max(points)

print(result)