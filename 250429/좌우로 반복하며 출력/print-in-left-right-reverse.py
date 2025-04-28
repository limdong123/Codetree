n = int(input())

a = []

for i in range(n):
    x = []
    for j in range(n):
        if(i%2 == 1):
            x.append(n-j)
        else:
            x.append(j+1)
    a.append(x)

for i in range(n):
    for j in range(n):
        print(a[i][j], end="")
    print()
