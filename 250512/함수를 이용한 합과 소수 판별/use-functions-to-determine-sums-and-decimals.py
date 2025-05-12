a, b = map(int, input().split())

# Please write your code here.
def fun1(n): #소수면서 자릿수합이 짝수
    if(if_decimal(n) and if_even(n)):
        return True
    else:
        return False

def if_decimal(n): #소수
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True

def if_even(n): #자릿수 합 짝수
    sum = 0
    while(n > 0):
        sum += n%10
        n = n//10

    if(sum%2 == 0):
        return True
    else:
        return False
    
cnt = 0
for i in range(a,b+1):
    if(fun1(i)):
        cnt += 1

print(cnt)
