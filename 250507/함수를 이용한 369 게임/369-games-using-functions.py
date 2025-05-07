a, b = map(int, input().split())

# Please write your code here.

def three_six_nine(a,b):
    cnt = 0
    for i in range(a, b+1):
        if(three_six_nine2(i) or i%3 == 0):
            cnt += 1
    return cnt


def three_six_nine2(n):
    boolean = False
    while(n > 0):
        temp = n%10
        n = n//10
        if(temp == 3 or temp == 6 or temp == 9):
            boolean = True
            break
    return boolean
            
result = three_six_nine(a,b)
print(result)
