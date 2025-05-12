n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def function(n):
    if n%2 == 0:
        print(n//2, end=" ")
    else:
        print(n, end=" ")

for i in range(n):
    function(arr[i])