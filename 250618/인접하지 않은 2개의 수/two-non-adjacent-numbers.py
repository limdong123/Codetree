n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

max_num = 0
for i in range(n):
    for j in range(i+2, n):
        max_num = max(max_num, (numbers[i] + numbers[j]))

print(max_num)