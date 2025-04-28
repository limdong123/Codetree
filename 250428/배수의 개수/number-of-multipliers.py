n = 10

numbers = [int(input()) for i in range(10)]
cnt_3 = 0
cnt_5 = 0

for i in numbers:
    if(i%3 == 0):
        cnt_3 += 1
    if(i%5 == 0):
        cnt_5 += 1

print(cnt_3, cnt_5)
