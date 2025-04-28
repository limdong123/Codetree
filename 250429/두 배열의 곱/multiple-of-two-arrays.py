
a = [list(map(int, input().split())) for _ in range(3)]
noe = input()
b = [list(map(int, input().split())) for _ in range(3)]

a_b = []
for i in range(3):
    for j in range(3):
        print(a[i][j] * b[i][j],end=" ")
    print()
    