n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
#arr 최소 공배수 -> arr 전부 곱하고 /2하면서 각 재귀마다 arr나눠지나 확인 
#안나눠 지면 다음 재귀로 나누워 ㅈ지면 min값에 넣기

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(arr):
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result


print(lcm_of_list(arr))