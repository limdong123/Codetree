a, b = map(int, input().split())
n = input()

# Please write your code here.
# a진수 n -> b진수 변환..

#10진수 변환
n_list = list(map(int, n))
num = 0
for i in range(len(n_list)):
    num = num * a + n_list[i] 

# b 진수 변환
result = []
while True:
    if num < b:
        result.append(num)
        break
    
    result.append(num%b)
    num //= b

#출력
for i in range(len(result) -1, -1, -1):
    print(result[i], end="")
