N = int(input())

# Please write your code here.
# n이 홀수 1-n까지의 홀수의 합
# n이 짝수 2-n까지의 짝수의 합


def f(n):
    if n <= 2:
        return n

    if n%2 == 0:
        return f(n-2) + n
    else:
        return f(n-2) + n

print(f(N))