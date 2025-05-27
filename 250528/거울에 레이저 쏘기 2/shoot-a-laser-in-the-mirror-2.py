n = int(input())
grid = [input().strip() for _ in range(n)]
k = int(input())

# 방향: 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작 좌표 및 방향 설정
def get_start_info(k):
    if 1 <= k <= n:
        return (0, k - 1, 2)  # 위에서 아래로 (남)
    elif n < k <= 2 * n:
        return (k - n - 1, n - 1, 3)  # 오른쪽에서 왼쪽 (서)
    elif 2 * n < k <= 3 * n:
        return (n - 1, 3 * n - k, 0)  # 아래에서 위로 (북)
    else:
        return (4 * n - k, 0, 1)  # 왼쪽에서 오른쪽 (동)

# 거울에 따른 방향 반사
# "/"  -> (위 -> 우), (우 -> 위), (하 -> 좌), (좌 -> 하)
# "\"" -> (위 -> 좌), (좌 -> 위), (하 -> 우), (우 -> 하)
def reflect(d, mirror):
    if mirror == '/':
        return [1, 0, 3, 2][d]
    else:  # '\'
        return [3, 2, 1, 0][d]

# 시뮬레이션
x, y, d = get_start_info(k)
count = 0
while 0 <= x < n and 0 <= y < n:
    mirror = grid[x][y]
    d = reflect(d, mirror)
    x += dx[d]
    y += dy[d]
    count += 1

print(count)
