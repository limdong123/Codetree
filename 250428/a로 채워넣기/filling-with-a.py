st = input()

for i in range(len(st)):
    if(i != 1 and i != len(st)-2):
        print(st[i],end="")
    else:
        print("a", end="")