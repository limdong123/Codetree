n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
class Point:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y
        

points_arr = []
for i in range(n):
    points_arr.append( Point(points[i][0], points[i][1][0], points[i][1][1]))

points_arr.sort(key = lambda x : (abs(x.x) + abs(x.y), x.idx))
for i in range(n):
    print(f"{points_arr[i].idx + 1}")