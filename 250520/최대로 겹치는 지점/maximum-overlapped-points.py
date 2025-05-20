n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

points = [0] * 101

for i in range(n):
    for j in range(segments[i][0], segments[i][1] + 1):
        points[j] += 1

result = max(points)
print(result)