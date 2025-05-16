n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str.sort()

cnt = 0
for i in str:
    temp_str = i
    if temp_str[0:2] == t:
        cnt += 1
        if cnt == k:
            print(temp_str)
            break

