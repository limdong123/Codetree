N, B = map(int, input().split())

# Please write your code here.

result_list = []

while True:
    if N < B:
        result_list.append(N)
        break
    
    result_list.append(N%B)
    N //= B

for i in range(len(result_list) -1, -1, -1):
    print(result_list[i],end="")