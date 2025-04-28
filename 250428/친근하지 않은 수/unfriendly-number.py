#친근한 수 조건  2 or 3 or 5로 나누어 지지 않는 수
n = int(input())
cnt = 0

for i in range(1, n+1):
    if(i%2 != 0 and i%3 != 0 and i%5 != 0):
        cnt += 1
    else:
        continue

print(cnt)