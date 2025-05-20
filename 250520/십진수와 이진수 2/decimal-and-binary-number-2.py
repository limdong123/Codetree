N = input()

# Please write your code here.
#10진수 변환 -> *17 -> 2진수 변환
n_list = list(map(int, N))

#10진수 변환
num = 0
for i in range(len(n_list)):
    num = num * 2 + n_list[i]

# * 17
num *= 17 

#2진수 변환
result = []
while True:
    if num < 2:
        result.append(num)
        break
    
    result.append(num%2)
    num //= 2

#출력
for i in range(len(result) -1, -1, -1):
    print(result[i], end="")
