n = int(input())

# Please write your code here.
def function1(n):
    if(n%2 == 0 and ((n//10)+(n%10))%5 == 0):
        print("Yes")
    else:
        print("No")

function1(n)
