A = input()

# Please write your code here.

def palindrome(a):
    for i in range(len(a)//2):
        if(a[i] != a[len(a) - i -1]):
            return False
    return True


if(palindrome(A)):
    print("Yes")
else:
    print("No")
        
