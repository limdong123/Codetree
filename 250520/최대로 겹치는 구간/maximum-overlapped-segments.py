n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#offset = 모든 수를 양수로 만들수 있는 수 = 100
offset = 100
points = [0] * (201)

for i in range(n):
    for j in range(segments[i][0] + offset, segments[i][1] + offset):
        points[j] += 1

result = max(points)

print(result)