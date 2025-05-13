n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result = 0

def f(n):
    global result
    if n == -1:
        return 0


    if arr[n] > result:
        result = arr[n]
    return f(n-1)

    
f(n-1)
print(result)