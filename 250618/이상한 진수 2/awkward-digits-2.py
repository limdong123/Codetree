a = input()

# Please write your code here.

a = list(map(int, a))

max_num = 0

for i in range(len(a)):
    if a[i] == 0:
        a[i] = 1
    else:
        a[i] = 0

    # 바꾸고 십진법 전환
    sum = 0
    for j in range(len(a)):
        sum += 2**(len(a) - 1 - j) * a[j]
    
    #최댓값 구하기
    max_num = max(max_num, sum)
    
    #초기화
    if a[i] == 0:
        a[i] = 1
    else:
        a[i] = 0

print(max_num)
    