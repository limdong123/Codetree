a,b,c = map(int, input().split())

if(a > b):
    if(b > c):
        print(b)
    elif(b < c):
        if(a > c):
            print(c)
        elif(a < c):
            print(a)
elif(a < b):
    if(a > c):
        print(a)
    elif(a < c):
        if(b > c):
            print(c)
        elif(b < c):
            print(b)
