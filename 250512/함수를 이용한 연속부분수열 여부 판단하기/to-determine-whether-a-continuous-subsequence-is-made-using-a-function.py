n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def fun1(i):
    for j in range(0, n2):
        if(a[j+i] != b[j]):
            return False
    return True


boolean = False
for i in range(0, n1 - n2 +1):
    if(fun1(i)):
        boolean = True

if(boolean):
    print("Yes")
else:
    print("No")

