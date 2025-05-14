n = int(input())

# Please write your code here.
#n이 짝수 /2 홀수 *3+1 n이 1 될때까지 반복 횟수

cnt = 0
def f(n):
    global cnt
    if n == 1:
        return 
    
    cnt += 1
    if n % 2 == 0:
        return f(n//2)
    else:
        return f(3*n + 1)
    

f(n)
print(cnt)
    