n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
# print(d, t) ['R', 'L', 'R'] [9, 3, 5]
# print(d2, t2) ['L', 'R', 'L', 'R'] [2, 2, 1, 12]

# 1초마 움직이는 위치 배열에 저장후 두개를 비교
A_arr = [0]
B_arr = [0]

# A 시뮬
now_point_a = 0
for i in range(n):
    for j in range(t[i]):
        #t만큼 d[i]방향으로 1씩 이동
        if d[i] == "R": # +
            now_point_a += 1
            A_arr.append(now_point_a)
        else :
            now_point_a -= 1
            A_arr.append(now_point_a)

now_point_b = 0
for i in range(m):
    for j in range(t2[i]):
        #t2만큼 d2[i]방향으로 1씩 이동
        if d2[i] == "R": # +
            now_point_b += 1
            B_arr.append(now_point_b)
        else :
            now_point_b -= 1
            B_arr.append(now_point_b)

#A_arr, B_arr 비교후 index랑 값 같은 위치 찾기
min_len = min(len(A_arr), len(B_arr))
result = -1
for i in range(1, min_len):
    if A_arr[i] == B_arr[i]:
        result = i
        break

print(result)

