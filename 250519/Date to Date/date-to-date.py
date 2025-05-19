m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
#          1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_is(m, d):
    sum = 0
    for i in range(m):
        sum += days[i]
    return sum + d

print(day_is(m2, d2) - day_is(m1, d1) + 1)