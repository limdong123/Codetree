n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
#n -> 1~n까지 크기,  k -> 반복횟수, com->커맨드

arr = []
for i in range(n+1):
    arr.append(0)


for i in range(k):
    for j in range(commands[i][0], commands[i][1] + 1):
        arr[j] += 1

max_num = 0
for e in arr:
    max_num = max(max_num, e)

print(max_num)