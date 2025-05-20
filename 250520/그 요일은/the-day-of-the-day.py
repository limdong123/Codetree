m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
#          1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def month_is(m, d):
    sum = 0
    for i in range(m):
        sum += month[i]
    return sum + d

a_day = month_is(m1, d1)
b_day = month_is(m2, d2)

result_day = b_day - a_day
for i in range(7):
    if days[i] == A:
        result_day - i 
        break

print(result_day%7)
