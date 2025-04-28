#1~100 까지 더하다 n보다 커지면 현재 숫자 출력
n = int(input())
temp = 0

while(n >= 0):
    temp += 1
    n = n - temp
    

print(temp)