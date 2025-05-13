N = int(input())

# Please write your code here.
def f(n):
    if n == 1:
        return 1
    
    #1 + 2 + 3 + ... + n-1 + n
    return f(n-1) + n

print(f(N))