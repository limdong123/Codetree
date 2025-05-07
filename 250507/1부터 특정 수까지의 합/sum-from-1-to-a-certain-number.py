n = int(input())

# Please write your code here.
def sum_n(n):
    num = 0
    for i in range(1,n+1):
        num += i
    
    return num//10

result = sum_n(n)
print(result)