li = ["apple", "banana", "grape", "blueberry", "orange"]

ch = input()
cnt = 0

for i in li:
    index = i[2:4].find(ch)
    if(index == -1):
        continue
    else:
        cnt += 1
        print(i)


print(cnt)
