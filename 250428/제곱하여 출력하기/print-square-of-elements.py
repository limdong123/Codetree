n = int(input())
num = list(map(int, input().split()))

num_ = [x**2 for x in num]
for i in num_:
    print(i, end=" ")