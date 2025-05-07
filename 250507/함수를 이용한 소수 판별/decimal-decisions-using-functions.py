a, b = map(int, input().split())

# Please write your code here.

#소수 판단 함수 
def 소수판단(n):
    for i in range(2,n-1):
        if(n%i == 0):
            return False
    return True


num_sum = 0
for i in range(a,b+1):
    if(소수판단(i)):
        num_sum += i
    else:
        continue
    
print(num_sum)