n, m = map(int, input().split())

# Please write your code here.

def lcm(n,m):
    min_ = n*m
    for i in range(1,n+1):
        for j in range(1, m+1):
            if(m*i == n*j and min_ > m*i):
                min_ = m*i
    print(min_)

lcm(n,m)
        