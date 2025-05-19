a, b, c, d = map(int, input().split())

# Please write your code here.

# 00시 00분 ~ c시 d분 - 00시 00분 ~ a시 b분
def time_is(h, m):
    return h * 60 + m

a_time = time_is(a,b)
b_time = time_is(c,d)

print(b_time - a_time)