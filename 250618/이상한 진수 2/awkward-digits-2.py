a = input()


# Please write your code here.
a = list(map(int, a))

for i in range(len(a)):
    if a[i] == 0:
        a[i] = 1
        break

result = 0
for i in range(len(a)):
    result += 2**(len(a) - i - 1) * a[i]

print(result)

