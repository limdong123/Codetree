n = int(input())

# Please write your code here.
def upper(n):
    if n == 0:
        return
    upper(n-1)
    print(n, end=" ")

def lower(n):
    if n == 0:
        return
    print(n, end=" ")
    lower(n-1)

upper(n)
print()
lower(n)
