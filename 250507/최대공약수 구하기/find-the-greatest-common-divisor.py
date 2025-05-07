n, m = map(int, input().split())

# Please write your code here.

def gcd(n,m):
    max = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(n%i == 0 and m%j == 0 and i == j):
                if(max < i):
                    max = i

    print(max)

gcd(n,m)
