N = int(input())

# Please write your code here.
def f(n):
    if n < 1:
        return 0
    return f(n//10) + (n%10)**2

print(f(N))