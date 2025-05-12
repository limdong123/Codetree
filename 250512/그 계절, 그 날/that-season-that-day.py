Y, M, D = map(int, input().split())

# Please write your code here.
# 1 3 5 7 8 10 12 => 31
# 4 6 9 11 => 30
# 2 => 28
# 3-5봄  6-8여름  9-11가을  12-2겨울

#존재하는 날짜
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
        if(leap):
            if(d > 29):
                return False
        else:
            if(d > 28):
                return False
    return True

#윤년 판단 
def is_leap_year(y):
    if(y%4 != 0): #4의 배수가 아니면
        return False
    elif(y%100 == 0 and y%400 == 0): 
        return True
    elif(y%100 == 0):
        return False
    else:
        return True
    

#계절 판단 
def is_season(m):
    if 3 <= m <= 5:
        print("Spring")
    elif 6 <= m <= 8:
        print("Summer")
    elif 9 <= m <= 11:
        print("Fall")
    else:
        print("Winter")

leap = False
is_days = False

if(is_leap_year(Y)):
    leap = True
else:
    leap = False

is_days = month_day(M, D)
if(is_days):
    is_season(M)
else:
    print(-1)
    