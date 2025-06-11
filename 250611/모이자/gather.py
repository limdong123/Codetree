n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
# x  --  1  2  3  4  5
# A  --  1  2  3  2  6

min_sum = 10000000

for i in range(n):
    now_home = A[i]

    sum_diff = 0
    for j in range(n):
        sum_diff += abs(j - i) * A[j]
    
    min_sum = min(min_sum, sum_diff)

print(min_sum)
            