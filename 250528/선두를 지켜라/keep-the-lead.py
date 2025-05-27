n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
#  n,m -> 4,3 
# 시간만다 거리를 배열에 담아 두개 비교해서 선두 바뀌는 떼 계산하기
A_arr = [0]
B_arr = [0]

now_point_a = 0
for i in range(n):
    for j in range(t[i]):
        now_point_a += v[i]
        A_arr.append(now_point_a)
    
now_point_b = 0
for i in range(m):
    for j in range(t2[i]):
        now_point_b += v2[i]
        B_arr.append(now_point_b)

cnt = 0
min_time = min(len(A_arr), len(B_arr))
first = ""

for i in range(1, min_time):
    if A_arr[i] < B_arr[i]:
        if first == "A":
            first = "B"
            cnt += 1
        elif first == "" :
            first = "B"

    elif A_arr[i] > B_arr[i]:
        if first == "B":
            first = "A"
            cnt += 1
        elif first == "":
            first = "A"
print(cnt)

# print(A_arr)
# print(B_arr)