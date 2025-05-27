n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans, cnt = 0, 0
for i in range(n):
    if i >= 1 and arr[i-1] > t and arr[i] > t:
        cnt += 1
    else :
        cnt = 1
    ans = max(ans, cnt)
print(ans)