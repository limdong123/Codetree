M, D = map(int, input().split())

# Please write your code here.
# 1 3 5 7 8 10 12 => 31
# 4 6 9 11 => 30
# 2 => 28


def month_day(m,d):
    if(1 <= m <= 12):
        if(day_is_t(m,d)):
            return True
    return False

def day_is_t(m,d):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if(d > 31):
            return False
    elif m in [4, 6, 9, 11]:
        if(d > 30):
            return False
    elif m in [2]:
        if(d > 28):
            return False
    return True



if month_day(M,D) :
    print("Yes")
else:
    print("No")