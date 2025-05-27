n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
#직전에 다른 위치 -> 현재 같은 위치 cnt, (같은위치 -> 같은위치 X, 하나가 끝난 이후에도 계속 세기)
A_arr = [0]
B_arr = [0]

now_point_a = 0
for i in range(n):
    for j in range(t[i]):
        if d[i] == "R":
            now_point_a += 1
            A_arr.append(now_point_a)
        else : 
            now_point_a -= 1
            A_arr.append(now_point_a)

now_point_b = 0
for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == "R":
            now_point_b += 1
            B_arr.append(now_point_b)
        else : 
            now_point_b -= 1
            B_arr.append(now_point_b)

# print(A_arr)        [0, -1, -2, -3, -2, -1, 0, 1, 2, 1, 2, 3]
# print(B_arr)        [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2]

cnt = 0
min_len = 0
min_arr = ""
if len(A_arr) > len(B_arr):
    min_len = len(B_arr)
    min_arr = "B"
else :
    min_len = len(A_arr)
    min_arr = "A"
last_point = 0
for i in range(1, min_len):
    if A_arr[i-1] != B_arr[i-1] and A_arr[i] == B_arr[i]:
        cnt += 1
    if i == min_len - 1:
        if len(A_arr) > len(B_arr):
            last_point = B_arr[i]
        else:
            last_point = A_arr[i] 

# 나머지 돌기 
if min_arr == "B":
    for i in range(len(B_arr), len(A_arr)):
        if A_arr[i-1] != last_point and A_arr[i] == last_point:
            cnt +=1
else :
    for i in range(len(A_arr), len(B_arr)):
        if B_arr[i-1] != last_point and B_arr[i] == last_point:
            cnt +=1

print(cnt)