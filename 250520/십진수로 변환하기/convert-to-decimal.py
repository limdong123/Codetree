binary = input()

# Please write your code here.
#2진수는   ---> 방향으로 바꾸든  <----방향으로 바꾸든 똑같다

a = list(map(int, binary))
num = 0
for i in range(len(binary)):
    num = num * 2 + a[i]
print(num)