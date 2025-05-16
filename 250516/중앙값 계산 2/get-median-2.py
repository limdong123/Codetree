n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
#홀수 번쨰 원소에서 
#지금까지 입력받은 값의 중앙 값 // 그때마다 sort해서 중앙값 찾기

def f_sort(arr):
    arr.sort()
    return arr[len(arr)//2]

result = []
temp_arr = []
for i in range(len(arr)):
    temp_arr.append(arr[i])
    if i % 2 == 0: # 홀수면(+1해야 하므로 짝수일때로 계산)
        result.append(f_sort(temp_arr))

for i  in result:
    print(i, end=" ")