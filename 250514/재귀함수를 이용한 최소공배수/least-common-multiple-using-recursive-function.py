n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
#모든 원소에 대해 n번째 원소부터 첫번쨰 원소까지 비교하며
#최소공배수를 구해 그 값을 반환하는 재귀함수를 작성하여 해결합니다.

def lcm(a,b): #최소공배수 구하여 반환
    gcd = 1 #최소공배수
    for i in range(1, min(a,b) + 1):
        if a%i == 0 and b % i == 0:
            gcd = i
    return a * b // gcd



def get_lcm_all(index):
    if index == 1:
        return arr[1]

    return lcm(get_lcm_all(index-1), arr[index])

print(get_lcm_all(n-1))