h,w = map(int, input().split())

b = int(w/((h/100)**2))

if(b >=25):
    print(b)
    print("Obesity")
else:
    print(b)
