n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def f(n):
    if n == -1:
        return 0

    return max(f(n-1), arr[n])

    
print(f(n-1))