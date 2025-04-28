a,b = map(int, input().split())

result = [0 for i in range(10)]
result[0] = a
result[1] = b

for i in range(2, len(result)):
    result[i] = (result[i-2] + result[i-1])%10

for i in result:
    print(i, end=" ")
    
