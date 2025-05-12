n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def absolute(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

absolute(arr)
for e in arr:
    print(e, end=" ")
