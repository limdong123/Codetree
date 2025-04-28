n = int(input())

a = [list(0 for _ in range(n)) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(i%2 == 0):
            a[j][i] = j+1
        else:
            a[j][i] = n-j

for i in range(n):
    for j in range(n):
        print(a[i][j], end="")
    print()
    