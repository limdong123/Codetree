n = int(input())

# Please write your code here.
list_n = []

while True:
    if n < 2:
        list_n.append(n)
        break
    
    list_n.append(n%2)
    n //= 2

for i in range(len(list_n)-1, -1, -1):
    print(list_n[i], end = "")
