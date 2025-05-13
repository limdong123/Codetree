N = int(input())

# Please write your code here.
#n이 짝수면 /2 홀수면 /3 -> 1이 되면 그때까지 진행한 작업 횟수 출력
result = 0
def f(n):
    if n == 1:
        return result
    
    if n%2 == 0:
        return f(n//2) + result + 1
    else :
        return f(n//3) + result + 1
    
result = f(N)
print(result)
    
    