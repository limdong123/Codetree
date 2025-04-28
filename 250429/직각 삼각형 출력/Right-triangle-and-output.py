n = int(input())

# 0 -> 1, 1->3, 3->5, 4*2-1->7, 5*2-1->9
for i in range(1, n+1):
    for j in range(0, i*2-1):
        print("*", end="")
    print()