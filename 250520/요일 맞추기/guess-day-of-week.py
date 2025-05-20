m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
#          1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def day_is(m, d):
    sum = 0
    for i in range(m):
        sum += month[i]
    return sum + d

a_day = day_is(m1, d1)
b_day = day_is(m2, d2)

result_day = b_day - a_day + 1

result_day %= 7
print(days[result_day])