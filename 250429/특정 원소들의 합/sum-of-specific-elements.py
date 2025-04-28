a = [list(map(int, input().split())) for _ in range(4)]

total = 0
for i in range(1, 5):
    for j in range(i):
        total += a[i-1][j]
print(total)
