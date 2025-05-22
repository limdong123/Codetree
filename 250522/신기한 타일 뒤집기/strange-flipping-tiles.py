n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
#R -> 현재 타일 포함 검은색,  L -> 현재 타일 포함 흰색
offset = 1000*100
maps = [""] * offset * 2
cur = offset

for i in range(n):
    if dir[i] == "R":
        for j in range(cur, cur + x[i]):
            maps[j] = "B"
        cur = cur + x[i] -1
    else :
        for j in range(cur, cur - x[i], -1):
            maps[j] = "W"
        cur = cur - x[i] + 1
    # W , B
cnt = [0, 0]
for i in maps:
    if i == "B":
        cnt[1] += 1
    elif i == "W":
        cnt[0] += 1

print(cnt[0], cnt[1])

