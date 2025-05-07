a, b, c = map(int, input().split())

# Please write your code here.
def min_(a,b,c):
    min_num = 101
    for i in [a,b,c]:
        if(min_num > i):
            min_num = i
    
    return min_num

print(f"{min_(a,b,c)}")
