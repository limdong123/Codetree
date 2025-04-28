# 홀 -> 2배
# 짝 -> +3

a,b = map(int, input().split())

while(True):
    if(a > b):
        break
    else:
        print(a, end =" ")
        if(a %2 == 1):
            a *= 2
        else:
            a += 3