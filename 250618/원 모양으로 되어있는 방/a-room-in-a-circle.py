n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
# 4 7 8 6 4
min_range = float('inf')
for i in range(n):
    
    temp_a = a[i+1:] + a[:i]
    
    total = 0
    for j in range(n-1):
        total += temp_a[j]*(j+1)

    min_range = min(min_range, total)

print(min_range)
        


        
    