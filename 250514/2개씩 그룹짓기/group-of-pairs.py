n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
# [i , 2n - i - 1] 조합일때 최댓값이 가장 작아짐
nums.sort()

result = 0
for i in range(0, n):
    result = max(result, nums[i] + nums[2*n - i - 1])
print(result)

