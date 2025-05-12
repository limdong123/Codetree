a, b = map(int, input().split())

# Please write your code here.
#작은 수 -> +10 , 큰 수 -> *2

def f(a,b):
    if a > b :
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return a,b

a,b = f(a,b)
print(a,b)