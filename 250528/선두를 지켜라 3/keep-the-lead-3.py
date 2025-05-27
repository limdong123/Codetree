N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
# 이번엔 중복도 조합한다
# ex) a -> a,b -> b -> a,b -> a  = 5

A_arr = [0]
B_arr = [0]

# A
now_point_a = 0
for i in range(N):
    for j in range(t[i]):
        now_point_a += v[i]
        A_arr.append(now_point_a)

now_point_b = 0
for i in range(M):
    for j in range(t2[i]):
        now_point_b += v2[i]
        B_arr.append(now_point_b)

# print(A_arr) [0, 1, 2, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
# print(B_arr) [0, 2, 4, 6, 7, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]


#조건 -> a나 b가 선두로 바뀐경우 cnt, a또는 B가 공동 선두가 된경우 cnt
cnt = 0

for i in range(1, len(A_arr)):
    if A_arr[i-1] >= B_arr[i-1] and A_arr[i] < B_arr[i]:
        cnt += 1
    if A_arr[i-1] <= B_arr[i-1] and A_arr[i] > B_arr[i]:
        cnt += 1

    if  A_arr[i-1] != B_arr[i-1] and A_arr[i] == B_arr[i]:
        cnt += 1


print(cnt)
