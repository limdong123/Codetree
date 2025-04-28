n = int(input())

# 홀수 and 3의 배수          or   짝수 and 5의 배수
if(n%2 != 0 and n%3 == 0) or (n%2 == 0 and n%5 == 0):
    print("true") 
else:
    print("false")