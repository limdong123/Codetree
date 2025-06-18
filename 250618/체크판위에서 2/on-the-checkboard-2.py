R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

first_color = grid[0][0]
end_color = grid[R-1][C-1]
cnt = 0

for i in range(1, R - 2):
    for j in range(1, C - 2):
        for i2 in range(i+1, R - 1):
            for j2 in range(j+1, C - 1):
                if grid[i][j] != first_color and grid[i2][j2] != grid[i][j] and grid[i2][j2] != end_color:
                    cnt += 1

print(cnt)