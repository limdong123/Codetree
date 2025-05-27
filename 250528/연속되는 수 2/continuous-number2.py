n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

num = arr[0]
cnt = 1
cnt_arr = []
for i in range(1, len(arr)):
    if arr[i] != num or i == len(arr) - 1:
        num = arr[i]
        cnt_arr.append(cnt + 1)
        cnt = 0
    else :
        cnt += 1

result = 0
if cnt_arr == []:
    result = 1
else : 
    result = max(cnt_arr)
print(result)