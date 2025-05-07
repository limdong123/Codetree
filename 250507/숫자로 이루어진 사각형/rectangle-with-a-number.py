n = int(input())

# Please write your code here.
def print_n(n):
    num = 0
    for _ in range(n):
        for _ in range(n):
            num = (num + 1)%10
            if(num == 0):
                num += 1
            print(num, end=" ")
        print()

print_n(n)