a, b, c = map(int, input().split())

# Please write your code here.
# 분 = c
# 시 = b*60
# 일 = a * 60 * 24

result = (a*60*24 + b*60 + c) -(11*60*24 + 11*60 + 11)
if result < 0:
    print(-1)
else:
    print(result)