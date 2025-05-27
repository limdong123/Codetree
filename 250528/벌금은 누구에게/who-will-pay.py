N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
cnt_arr = [0] * (N + 1)
temp = False
for i in range(M):
    cnt_arr[student[i]] += 1
    if K == max(cnt_arr):
        temp = True
        break

if temp:
    for i in range(N):
        if cnt_arr[i] == K:
            print(i)
            break
else :
    print(-1)
