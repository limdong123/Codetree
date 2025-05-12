a, b = map(int, input().split())

# 온전수 판단해서 t,f 리턴
def function1(n):
    if(n%2 == 0):
        return False
    elif(n%10 == 5):
        return False
    elif(n%3 == 0 and n%9 != 0):
        return False
    else:
        return True


num = 0
boolean = False
for i in range(a,b+1):
    boolean = function1(i)
    if(boolean):
        num += 1
        boolean = False

print(num)
    


