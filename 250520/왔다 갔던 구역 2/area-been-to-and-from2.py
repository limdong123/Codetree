n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
# offset 1000
points = [0] * 2000
offset = 1000
temp_point = offset

for i in range(n):
    if dir[i] == "R":
        for j in range(temp_point, temp_point + x[i]):
            points[j] += 1
        temp_point = temp_point + x[i] 
    else:
        for j in range(temp_point, temp_point - x[i], -1):
            points[j] += 1
        temp_point = temp_point - x[i]

cnt = 0
for e in points:
    if e >= 2:
        cnt += 1
print(cnt)