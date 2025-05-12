A = input()

# Please write your code here.
def f(a):
    for i in range(1, len(a)):
        if a[0] != a[i]:
            return False
    return True

if(f(A)):
    print("No")
else:
    print("Yes")