n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# a,b,c 3개의 수 골라
# 각 자릿수의 합이 10이 넘으면 carry발생
# 각 자릿수의 합이 10이 넘지 않는 것들중 최대값 구하기

max_num = -1

#3개 숫자 고르는 배열
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            
            a,b,c = arr[i], arr[j], arr[k]
            now_num = a+b+c
            for _ in range(4):
                if a%10 + b%10 + c%10 < 10:
                    a //= 10
                    b //= 10
                    c //= 10
                else:
                    now_num = 0
            max_num = max(max_num, now_num)

print(max_num)
            



            