a, b, c = map(int, input().split())

# Please write your code here.
def f(n):
    if n < 1:
        return 0
    
    return f(n//10) + (n % 10)

num = a * b * c
print(f(num))

