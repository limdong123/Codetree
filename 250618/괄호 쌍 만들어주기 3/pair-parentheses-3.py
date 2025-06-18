A = input()

# Please write your code here.
#처음부터 '(' 인지 확인하는 배열
# ( 발견하면 이후  ) 나오는거 cnt 

cnt = 0 

for i in range(len(A) - 1):
    if A[i] == '(':
        for j in range(i + 1, len(A)):
            if A[j] == ')':
                cnt += 1

print(cnt)
